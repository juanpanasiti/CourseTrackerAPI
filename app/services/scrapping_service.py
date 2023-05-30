from typing import Tuple

from app.external_interfaces.platzi_ei import PlatziEI
from app.helpers import scrapping_helpers
from app.repositories.school_repository import SchoolRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.author_repository import AuthorRepository
from app.database.models.school_model import SchoolModel
from app.database.models.course_model import CourseModel
from app.database.models.author_model import AuthorModel



class ScrappingService():
    def __init__(self) -> None:
        self.platzi_ei = PlatziEI()
        self.school_repo = SchoolRepository()
        self.course_repo = CourseRepository()
        self.autor_repo = AuthorRepository()

    def update_schools(self) -> Tuple[int,int,int]:
        courses_page:str = self.platzi_ei.get_page('/cursos/')

        scrapped_schools = scrapping_helpers.get_schools_data(courses_page)
        new_schools_counter = 0
        new_course_counter = 0
        new_author_counter = 0

        for school in scrapped_schools:
            filter_course = {
                'platzi_id': school.platzi_id
            }

            # Add school to DB if not exists
            school_db = self.school_repo.get_one_by_filter(filter_course)
            if school_db is None:
                school_db = SchoolModel()
                school_db.category = school.category
                school_db.name = school.name
                school_db.description = school.description
                school_db.platzi_id = school.platzi_id
                school_db.route_url = school.route_url
                school_db.about = school.about
                school_db.badge_url = school.badge_url

                try:
                    self.school_repo.create(school_db)
                    new_schools_counter += 1
                except Exception as ex:
                    print('\033[91m', f'No se pudo cargar la escuela {school.name}', '\033[0m')
                    print('\033[91m', f'Error tipo {type(ex)}', '\033[0m')
                    print('\033[91m', f'{ex.args}', '\033[0m')

            for course in school.courses:
                filter_course = {
                    'platzi_id': course.platzi_id
                }
                filter_author = {
                    'fullname': course.author.fullname
                }
                course_db = self.course_repo.get_one_by_filter(filter_course)
                author_db = self.autor_repo.get_one_by_filter(filter_author)

                if author_db is None:
                    author_db = AuthorModel()
                    author_db.fullname = course.author.fullname
                    author_db.platzi_id = course.author.platzi_id
                    author_db.bio = course.author.bio
                    author_db.about = course.author.about
                    author_db.photo_url = course.author.photo_url
                    author_db.profile_url = course.author.profile_url

                    try:
                        self.autor_repo.create(author_db)
                        new_author_counter += 1
                    except Exception as ex:
                        print('\033[91m', f'No se pudo cargar el autor {course.author.fullname}', '\033[0m')
                        print('\033[91m', f'Error tipo {type(ex)}', '\033[0m')
                        print('\033[91m', f'{ex.args}', '\033[0m')

                if course_db is None:
                    course_db = CourseModel()
                    
                    course_db.title = course.title
                    course_db.description = course.description
                    course_db.level = course.level
                    course_db.platzi_id = course.platzi_id
                    course_db.platzi_url = course.platzi_url
                    course_db.status = course.status
                    course_db.is_active = course.is_active
                    course_db.score = course.score
                    course_db.badge_url = course.badge_url
                    course_db.first_class_url = course.first_class_url
                    course_db.author_id = author_db.id if (author_db and author_db.id) else None

                    try:
                        self.course_repo.create(course_db)
                        new_course_counter += 1
                    except Exception as ex:
                        print('\033[91m', f'No se pudo cargar el curso {course.title}', '\033[0m')
                        print('\033[91m', f'Error tipo {type(ex)}', '\033[0m')
                        print('\033[91m', f'{ex.args}', '\033[0m')
        
        return new_schools_counter, new_course_counter, new_author_counter