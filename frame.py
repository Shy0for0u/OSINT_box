import full_scripts.host_ip
import full_scripts.geo
import full_scripts.whois_add
import full_scripts.site_nslookup
import full_scripts.dns_resolver
import full_scripts.reversed_dns
import full_scripts.robots
import full_scripts.sitemap
import full_scripts.reverse_ip_lookup
from colorama import Fore, init


def layout(arg):
    return (
    "+" + "-" * 60 + "+" + "\n" +
    "{}{:^60}{}".format('|', OsintBox.name_functions[arg], '|\n') +
    "+" + "-" * 60 + "+")


def design_of_output(func):
    def wrapper(*args):
        print(layout(args[1]))
        func(*args)
    return wrapper


class OsintBox:
    init(convert=True)
    name_functions = {
            0: "Exit the program",
            1: "Host IP",
            2: "Site location",
            3: "Whois",
            4: "Nslookup",
            5: "DNS MX - Record",
            6: "Reverse DNS",
            7: "robots.txt",
            8: "sitemap.xml",
            9: "Reverse ip lookup",
            10: "All items"
        }

    choices = {
        0: None,
        1: full_scripts.host_ip.host_ip,
        2: full_scripts.geo.site_location,
        3: full_scripts.whois_add.whois_add,
        4: full_scripts.site_nslookup.nslookup_site,
        5: full_scripts.dns_resolver.dns_mx_record,
        6: full_scripts.reversed_dns.reverse_dns,
        7: full_scripts.robots.get_robot_txt,
        8: full_scripts.sitemap.sitemap,
        9: full_scripts.reverse_ip_lookup.reverse_ip_lookup
    }

    input_data = {
        1: "Enter host: ",
        2: "Enter ip: ",
        3: "Enter domain: ",
        4: "Enter host: ",
        5: "Enter host: ",
        6: "Enter ip: ",
        7: "Enter host [https://site.com]: ",
        8: "Enter host [https://site.com]: ",
        9: "Enter IP or Domain: ",
        10: "Enter host "
    }

    def __init__(self):
        self.start_menu()
        self.make_a_choice()

    def start_menu(self):
        print(
            Fore.GREEN + r'''
              ___  ____ ___ _   _ _____   ____   _____  __
             / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
            | | | \___ \| ||  \| | | |   |  _ \| | | \  / 
            | |_| |___) | || |\  | | |   | |_) | |_| /  \ 
             \___/|____/___|_| \_| |_|   |____/ \___/_/\_\

        0.  Exit the program
        1.  Host IP
        2.  Site location
        3.  Whois
        4.  Nslookup
        5.  DNS MX-Record
        6.  Reverse DNS
        7.  robots.txt
        8.  sitemap.xml
        9.  Reverse ip lookup
        10. All items
        ''' + Fore.RESET)

    def all_items(self, domain):
        try:
            ip = self.choices[1](domain).split()[-1]
        except ValueError:
            print("error")
        else:
            with open("check_domain.txt", "w") as file:
                for index in range(1, 10):
                    if index in [1, 3, 4, 5, 9]:
                        data = f"{layout(index)}\n{self.choices[index](domain)}\n"
                    elif index in [7, 8]:
                        data = f"{layout(index)}\n{self.choices[index]('https://' + domain)}\n"
                    else:
                        data = f"{layout(index)}\n{self.choices[index](ip)}\n"
                    file.writelines(data)

    @design_of_output
    def new_design(self, choice):
        value = input(self.input_data[choice])
        if choice == 10:
            self.all_items(value)
            print("Done!")
        else:
            output = self.choices[choice](value)
            print(output)

    def make_a_choice(self):
        while True:
            try:
                choice = int(input("\nEnter the option number: "))
                assert choice in self.name_functions.keys()
            except (AssertionError, TypeError, ValueError):
                print(Fore.RED +
                      "Error: Make a choice program from menu!" +
                      Fore.RESET)
            except (KeyboardInterrupt, AssertionError):
                print(Fore.GREEN + "\nThe program is complete!" + Fore.RESET)
                break
            else:
                if choice == 0:
                    print(Fore.GREEN + "\nThe program is complete!" + Fore.RESET)
                    break
                self.new_design(choice)


if __name__ == "__main__":
    OsintBox()

    # ctftime.org
    # 109.233.56.78
    # 77.88.55.55
    
    # for 7,8 part:
    # https://www.google.com
    # https://ctftime.org
    # https://cyber-ed.ru
    # https://yandex.ru

    # luxdevices.com
