def solution(id_list, report, k):
    mail_per_person = number_of_mails_received_per_person(id_list,report, k)
    times_received_mail = list(mail_per_person.values())
    return times_received_mail

def number_of_mails_received_per_person(id_list,report, k):
    received_mail_per_person = { person : 0 for person in id_list}
    reporters_by_reported_person = make_reporters_by_reported_person(id_list, report)
    for reported_person in id_list:
        if len(reporters_by_reported_person[reported_person])>=k:
            for reporter in reporters_by_reported_person[reported_person]:
                received_mail_per_person[reporter]+=1
    return received_mail_per_person

def make_reporters_by_reported_person(id_list, report):
    report_list = { reported_person:[] for reported_person in id_list}
    remove_duplicate_report = set(report)
    
    for report in remove_duplicate_report:
        [reporter, reported_person]= report.split()
        report_list[reported_person].append(reporter)
        
    return report_list
    