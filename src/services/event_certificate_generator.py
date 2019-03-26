from certificategen.entities.certificate_info import CertificateInfo
from certificategen.services.certificate_generator import CertificateGenerator
from src.domain.entities.event import Event
from src.repositories.event_repository import EventRepository
from src.repositories.participation_repository import ParticipationRepository


class EventCertificateGenerator(object):

    def generate_by_event_id(self, event_id: int):
        event_repository = EventRepository()
        participation_repository = ParticipationRepository()

        event = event_repository.get_by_id(event_id)
        participations = participation_repository.get_by_event_id(event_id)

        certificate_info = self.__build_certificate_info(event=event)

        certificate_generator = CertificateGenerator(certificate_info)

        for person in event.persons:
            if person.name:
                checkin = [participation for participation in participations if participation.person_id == person.id and participation.checkin]
                if checkin:
                    certificate_generator.generate(person.name)

    def __build_certificate_info(self, event: Event):
        event_name = event.name
        event_type = "evento"
        action = "participou do"
        description = "O <organizer> certifica que <participant> <action> <event_type> <event_name> no dia <date>."
        date = event.local_date
        organizer = "GDG-Petrópolis"
        signature = "assets/signature.png"
        background = "assets/background.pdf"

        certificate_info = CertificateInfo(event_name=event_name, event_type=event_type, action=action,
                                           description=description, date=date, organizer=organizer, signature=signature,
                                           background=background)

        return certificate_info



