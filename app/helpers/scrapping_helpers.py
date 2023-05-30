import re
from typing import List, Tuple

from bs4 import BeautifulSoup, Tag

from app.external_interfaces.platzi_ei import PlatziEI
from app.core import settings
from app.schemas.school_schemas import SchoolBase
from app.schemas.course_schemas import CourseBase
from app.schemas.author_schemas import AuthorBase


def get_course_url_base(first_lesson_url):
    url = "/".join(first_lesson_url.split("/")[:4])
    url += f'/{"-".join(first_lesson_url.split("/")[4].split("-")[1:])}'
    return url


def get_first_lesson_url(url):
    page = PlatziEI().get_page(url)
    soup = BeautifulSoup(page, "html.parser")
    return (
        settings.PLATZI_URL
        + soup.find_all("div", attrs={"class": "ContentClass"})[0].a["href"]
    )


def get_courses_from_school(school:Tag)->List[CourseBase]:
    # Extraer información de los cursos
    courses_div = school.find('div', class_='School-courses')
    course_links = courses_div.find_all('a', class_='Course')

    courses: List[CourseBase] = []
    for link in course_links:
        course_title = link.find('h4').text.strip()
        author_fullname = link.find('p').text.replace('Por', '').strip()
        badge_url = link.find('img').get('src')
        href_url = link.get('href')
        try:
            platzi_id = int(re.findall(r"/(\d+)-", href_url)[0])
        except:
            platzi_id = 0
        if platzi_id == 0:
            url = settings.PLATZI_URL + href_url
            try:
                first_lesson_url = get_first_lesson_url(href_url)
            except Exception as ex:
                first_lesson_url = ""
                print('\033[91m', url, '\033[0m')
                print('\033[91m', ex.args, '\033[0m')
            try:
                platzi_id = int(re.findall(r"/(\d+)-", first_lesson_url)[0])
            except Exception as ex:
                print('\033[31m', f'Error with course {url}', '\033[0m')
                
        else:
            first_lesson_url = settings.PLATZI_URL + href_url
            url = get_course_url_base(first_lesson_url)
        course = CourseBase()
        course.title = course_title
        course.badge_url = badge_url
        course.first_class_url = first_lesson_url
        course.platzi_id = platzi_id
        course.platzi_url = url
        course.author.fullname = author_fullname

        courses.append(course)

    return courses

def get_schools_from_category(category_tag: Tag) -> List[SchoolBase]:
    h2 = category_tag.find('h2')
    
    # Encontrar la etiqueta <span> dentro del h2 y extraer su texto
    span = h2.find('span')
    category_title = span.text.strip()

    schools: List[SchoolBase] = []

    school_divs = category_tag.find_all('div', class_='School')

    for school_div in school_divs:
        img_src: str = school_div.select_one('.School-header-title a figure img')['src']
        header_title: str = school_div.select_one('.School-header-title a h3').text.strip()
        href: str = school_div.select_one('.School-header-title a')['href']
        description: str = school_div.select_one('.School-header p').text.strip()

        school_item = SchoolBase()
        school_item.category = category_title
        school_item.name = header_title
        school_item.description = description
        school_item.platzi_id = href.replace('/ruta/','').replace('/','')
        school_item.route_url = href
        school_item.about = ''
        school_item.badge_url = img_src
    
        school_item.courses = get_courses_from_school(school_div)
        

        schools.append(school_item)

    return schools


def get_schools_data(page: str) -> List[SchoolBase]:
    soup = BeautifulSoup(page, 'html.parser')

    # Encontrar el tag <section> con el atributo class='Categories'
    categories_section = soup.find('section', class_='Categories')

    # Encontrar todos los <div> con el atributo class='Categories-item' dentro del tag <section> encontrado
    categories = categories_section.find_all('div', class_='Categories-item')
    
    response: List[SchoolBase] = []
    for category in categories:
        schools = get_schools_from_category(category)
        response.extend(schools)

    return response
