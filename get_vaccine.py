from doctolib import Doctolib
from multiprocessing import Process


pollTime = 5
retryCount = 8640  # Will run for 12 hours by retrying every 5 seconds

grassl = (
    "Dr.Grassl-Sendling",
    "https://www.doctolib.de/availabilities.json?start_date={}&visit_motive_ids=2760330&agenda_ids=454126&insurance_sector=public&practice_ids=116543&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?speciality_id=5593&practitioner_id=any",
    pollTime,
    retryCount
)

mvzlaim = (
    "MVZ-Impfzentrum-Laim",
    "https://www.doctolib.de/availabilities.json?start_date={}&visit_motive_ids=2742628&agenda_ids=447527&insurance_sector=public&practice_ids=175048&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/medizinisches-versorgungszentrum-mvz/muenchen/medizinisches-versorgungszentrum-mvz-laim-gmbh?speciality_id=5593&practitioner_id=any",
    pollTime,
    retryCount
)

hausarztglockenbachviertel = (
    "Hausarzt-Glockenbachviertel",
    "https://www.doctolib.de/availabilities.json?start_date= {}&visit_motive_ids=2767063&agenda_ids=450406&insurance_sector=public&practice_ids=106858&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/praxis/muenchen/hausarztpraxis-muenchen?speciality_id=5593&practitioner_id=any",
    pollTime,
    retryCount
)


if __name__ == "__main__":
    processList = [
        Process(target=Doctolib(*grassl).main),
        Process(target=Doctolib(*mvzlaim).main),
        Process(target=Doctolib(*hausarztglockenbachviertel).main)
    ]
    # Start
    for p in processList:
        p.start()
    # Join
    for p in processList:
        p.join()
