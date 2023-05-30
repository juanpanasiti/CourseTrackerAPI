from app.services.scrapping_service import ScrappingService
class ScrappingController():
    def __init__(self) -> None:
        self.scrapping_service = ScrappingService()

    def scrap_schools(self):
        new_schools, new_courses, new_authors = self.scrapping_service.update_schools()
        # new_courses, new_authors = self.scrapping_service.update_courses_authors()
        return {
            'new_schools': new_schools,
            'new_courses': new_courses,
            'new_authors': new_authors,
        }