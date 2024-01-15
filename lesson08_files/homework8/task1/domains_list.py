def write_domains_into_list(processed_file):
    with open(processed_file, 'r') as file:
        domain_names = [line.strip() for line in file]
        return [domain.replace('.', '') for domain in domain_names]


file_name = "domains.txt"
domains_list = write_domains_into_list(file_name)
print("Cписок назв доменів у файлі domains.txt: ")
print(domains_list)
