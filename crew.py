import socket

def check_domain(domain_name):
    try:
        print(f"Domain {domain_name} kullanılıyor.")
    except socket.gaierror:
        print(f"Domain {domain_name} kullanılmıyor veya bulunamadı.")

domain_to_check = input('Domain: ')
check_domain(domain_to_check)

# Normalde tüm site bilgilerini yazdırıcaktım ancak github'da illegal sıkıntısı olduğu için yapmadım. Bu kod crew tarafından kodlandı, paylaşılması yasaktır.
