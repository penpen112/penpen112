import os
import time
import sys

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

WISATA_JATIM = {
    "Bangkalan": [
        {"nama": "Bukit Jaddih", "link": "https://maps.app.goo.gl/FJVkbvMBjypyzts48"},
        {"nama": "Pantai Siring Kemuning", "link": "https://maps.app.goo.gl/CDGqELoBXnrKSBEY9"},
        {"nama": "Mercusuar Sembilangan", "link": "https://maps.app.goo.gl/39TdTahrmNjXvtCC6"},
        {"nama": "Alun-Alun Taman Paseban", "link": "https://maps.app.goo.gl/dCP1QrfCSMTeaFAy5"}
    ],
    "Banyuwangi": [
        {"nama": "Kawah Ijen", "link": "https://maps.app.goo.gl/Zo7fcx8t6QoGqv7P6"},
        {"nama": "Pantai Pulau Merah", "link": "https://maps.app.goo.gl/vK4CnvDjAJ23Kcay7"},
        {"nama": "Air Terjun Telunjuk Raung", "link": "https://maps.app.goo.gl/1c8V38iJfndtkgzK7"},
        {"nama": "Alas Purwo", "link": "https://maps.app.goo.gl/pnyPaWzqdRbUnG4J7"}
    ],
    "Blitar": [
        {"nama": "Makam Bung Karno", "link": "https://maps.app.goo.gl/ZS4B3acgbbSAARkNA"},
        {"nama": "Candi Penataran", "link": "https://maps.app.goo.gl/ZBPp8MRQgZGZ1pkAA"},
        {"nama": "Pantai Tambakrejo", "link": "https://maps.app.goo.gl/w4nV39WDVqyobf4FA"},
        {"nama": "Kampung Coklat", "link": "https://maps.app.goo.gl/kLSjkWTPVpojEzR46"}
    ],
    "Bojonegoro": [
        {"nama": "Kayangan Api", "link": "https://maps.app.goo.gl/2Lbc4QEP9Hc9N4HH7"},
        {"nama": "Bendungan Gerak", "link": "https://maps.app.goo.gl/se67TWBXosf2qQM98"},
        {"nama": "Agrowisata Kebun Belimbing", "link": "https://maps.app.goo.gl/Pb2Zb3PdREDGtqBg9"},
        {"nama": "Waduk Pacal", "link": "https://maps.app.goo.gl/Yxxq64WRuQA1BgoP9"}
    ],
    "Bondowoso": [
        {"nama": "Kawah Wurung", "link": "https://maps.app.goo.gl/bQQrBbcVRCGfNRYB9"},
        {"nama": "Kawah Ilalang", "link": "https://maps.app.goo.gl/omWtYuxsWWdFmKxH8"},
        {"nama": "Air Terjun Tancak Kembar", "link": "https://maps.app.goo.gl/vd9spUkMcpjn7opA7"},
        {"nama": "Pemandian Tasnan", "link": "https://maps.app.goo.gl/PhFdVcM6hc245i1U9"}
    ],
    "Gresik": [
        {"nama": "Makam Sunan Giri", "link": "https://maps.app.goo.gl/BvNgGmitCC9Wp8oi9"},
        {"nama": "Bukit Kapur Setigi", "link": "https://maps.app.goo.gl/zX3z6t9fxeFjYwHe9"},
        {"nama": "Pantai Delegan", "link": "https://maps.app.goo.gl/QLJUgG3twWyG32LP7"},
        {"nama": "Banyuurip Mangrove Center Ujungpangkah", "link": "https://maps.app.goo.gl/KsvWGQrPtQpHh6zXA"}
    ],
    "Jember": [
        {"nama": "Pantai Papuma", "link": "https://maps.app.goo.gl/d1hBkniNXhTjS2YEA"},
        {"nama": "Nusa Barung", "link": "https://maps.app.goo.gl/Wx8BjwUY3i7NF8Le8"},
        {"nama": "Wisata Kebun Teh Gunung Gambir", "link": "https://maps.app.goo.gl/MSKfsbapKibEeXXr7"},
        {"nama": "Taman Botani", "link": "https://maps.app.goo.gl/H4xou1WyS2J2V6Fo8"}
    ],
    "Jombang": [
        {"nama": "Makam Gus Dur", "link": "https://maps.app.goo.gl/zswy4R5RD9Q8kY666"},
        {"nama": "Kedung Cinet", "link": "https://maps.app.goo.gl/Pgi8hCHTA2s4aeXd6"},
        {"nama": "Air Terjun Tretes Pengajaran", "link": "https://maps.app.goo.gl/7ysEiqPB2D9gYmwD6"},
        {"nama": "Candi Rimbi", "link": "https://maps.app.goo.gl/TVjANVE9wzshNJE16"}
    ],
    "Kediri": [
        {"nama": "Gunung Kelud", "link": "https://maps.app.goo.gl/EAVqPPvfCEDuqepG7"},
        {"nama": "Simpang Lima Gumul", "link": "https://maps.app.goo.gl/vYsJwZd8MHXYV2fv8"},
        {"nama": "Goa Selomangleng", "link": "https://maps.app.goo.gl/yRH5g6Sdr7JTzmMq6"},
        {"nama": "Goa Jegles", "link": "https://maps.app.goo.gl/bYSTPXtLfD58mHDH6"}
    ],
    "Lamongan": [
        {"nama": "WBL", "link": "https://maps.app.goo.gl/x4foEoZxaJbVq5fD9"},
        {"nama": "Maharani Zoo & Goa", "link": "https://maps.app.goo.gl/8MVnr8oS6Kg2CKuH9"},
        {"nama": "Pantai Kutang", "link": "https://maps.app.goo.gl/8xJWZNDZmNkzATgq8"},
        {"nama": "Makam Sunan Drajat", "link": "https://maps.app.goo.gl/ztKYYha3VqWsGznD9"}
    ],
    "Lumajang": [
        {"nama": "Air Terjun Tumpak Sewu", "link": "https://maps.app.goo.gl/qJSLvYZFU9XPoWpH7"},
        {"nama": "Ranu Kumbolo", "link": "https://maps.app.goo.gl/MMFc8pZEMXpoyvBE9"},
        {"nama": "Puncak B29", "link": "https://maps.app.goo.gl/42CaZCbzG5qqstJr6"},
        {"nama": "Ranu Regulo", "link": "https://maps.app.goo.gl/5Snm8uUSChdRKpXY8"}
    ],
    "Madiun": [
        {"nama": "Pahlawan Street Center", "link": "https://maps.app.goo.gl/5rCeiGjyeLZ6sDji9"},
        {"nama": "Alun-Alun Madiun", "link": "https://maps.app.goo.gl/vJssh9GqNeQc1KgDA"},
        {"nama": "Monumen Kresek", "link": "https://maps.app.goo.gl/weNaCFZfo9vWovYu8"},
        {"nama": "Hutan Pinus NONGKO IJO", "link": "https://maps.app.goo.gl/PK4uxvGFS6mPEXA68"}
    ],
    "Magetan": [
        {"nama": "Telaga Sarangan", "link": "https://maps.app.goo.gl/r3BeoRjoD52T35ch8"},
        {"nama": "Mojosemi Forest Park", "link": "https://maps.app.goo.gl/gHW8AKuJkzjo7UXT6"},
        {"nama": "Genilangit", "link": "https://maps.app.goo.gl/oqtiGKiVWk1suGAK6"},
        {"nama": "Air Terjun Tirtosari", "link": "https://maps.app.goo.gl/W3yQNQQrEKiLZueu5"}
    ],
    "Malang": [
        {"nama": "Pantai Balekambang", "link": "https://maps.app.goo.gl/sz7froB7MvLway4F6"},
        {"nama": "Coban Rondo", "link": "https://maps.app.goo.gl/svXWsPgxiFdVjhSD7"},
        {"nama": "Agrowisata Teh Wonosari", "link": "https://maps.app.goo.gl/KqZKYapmdoE9uovg7"},
        {"nama": "Alun-Alun Tugu", "link": "https://maps.app.goo.gl/4r5xVGVSKivDZXNr5"}
    ],
    "Mojokerto": [
        {"nama": "Museum Majapahit", "link": "https://maps.app.goo.gl/nPLANaUuYTEnypAp6"},
        {"nama": "Candi Tikus", "link": "https://maps.app.goo.gl/E3DQ7h7jRJdSha6Y7"},
        {"nama": " Gunung Penanggungan", "link": "https://maps.app.goo.gl/DATCrypWiCvNsPFN7"},
        {"nama": "Aone Trawas", "link": "https://maps.app.goo.gl/ySmcqjwRopZuYpwv6"}
    ],
    "Nganjuk": [
        {"nama": "Wisata Nganjuk Jolotundo", "link": "https://maps.app.goo.gl/3J68kJDNKrkp8TxP6"},
        {"nama": "Roro Kuning", "link": "https://maps.app.goo.gl/hH6vDwXK8p6cwPaKA"},
        {"nama": "Bukit Batu", "link": "https://maps.app.goo.gl/YngLM4ktZWBXU2oL8"},
        {"nama": "Singokromo", "link": "https://maps.app.goo.gl/azYrZtCm3B5YQ3Be6"}
    ],
    "Ngawi": [
        {"nama": "Benteng Van Den Bosch", "link": "https://maps.app.goo.gl/XsKHXdVGjQSVcx4V9"},
        {"nama": "Srambang Park", "link": "https://maps.app.goo.gl/Fevp8dV2ZggVees18"},
        {"nama": "Museum Trinil", "link": "https://maps.app.goo.gl/zdMBGLCWyx8FXAnY6"},
        {"nama": "Sumber Koso", "link": "https://maps.app.goo.gl/2DNwkTDakCMsY6j6A"}
    ],
    "Pacitan": [
        {"nama": "Pantai Klayar", "link": "https://maps.app.goo.gl/N6cCbbbrQ9FfHczb7"},
        {"nama": "Goa Gong", "link": "https://maps.app.goo.gl/x7hcixRY8CTQ5g6e6"},
        {"nama": "Sungai Maron", "link": "https://maps.app.goo.gl/yCoEeH9zXnF86MnG9"},
        {"nama": "Pantai Kasap", "link": "https://maps.app.goo.gl/qjdTgyq6AxKpFp7Y6"}
    ],
    "Pamekasan": [
        {"nama": "Api Tak Kunjung Padam", "link": "https://maps.app.goo.gl/GWJm6xjiQJ6R8doz6"},
        {"nama": "Museum Mandhilaras", "link": "https://maps.app.goo.gl/cexh8aDGwyvNbx6d7"},
        {"nama": "Kampoeng Toron Samalem", "link": "https://maps.app.goo.gl/ioxceCurscbsKKYaA"},
        {"nama": "Bukit Kehi", "link": "https://maps.app.goo.gl/8fyPCPv1JQiydEsy6"}
    ],
    "Pasuruan": [
        {"nama": "Taman Safari Prigen", "link": "https://maps.app.goo.gl/S9CCMotoCt8zhrBw7"},
        {"nama": "Alun-Alun Pasuruan", "link": "https://maps.app.goo.gl/LpxdaxXnB2kryY7g6"},
        {"nama": "Danau Ranu Grati", "link": "https://maps.app.goo.gl/ZzBE3j1UEV1r9pu29"},
        {"nama": "Taman Kota Pasuruan", "link": "https://maps.app.goo.gl/99VP1mx4DafMztPS7"}
    ],
    "Ponorogo": [
        {"nama": "Telaga Ngebel", "link": "https://maps.app.goo.gl/ZD8LMfQesLptwBqL6"},
        {"nama": "Kampoeng Wisata Durian Ngrogung", "link": "https://maps.app.goo.gl/L4EBzacWRgCpDKXF8"},
        {"nama": "Air Terjun Pletuk", "link": "https://maps.app.goo.gl/3ex37tUmPVppk6YE8"},
        {"nama": "Gunung Bayangkaki", "link": "https://maps.app.goo.gl/VriyTs2TddgDbncp7"}
    ],
    "Probolinggo": [
        {"nama": "Gunung Argapura", "link": "https://maps.app.goo.gl/Vneamky1qyiqGKZb8"},
        {"nama": "Air Terjun Madakaripura", "link": "https://maps.app.goo.gl/o1BT4mAYRCXngb9a9"},
        {"nama": "BJBR", "link": "https://maps.app.goo.gl/ZrtvxtyZH9Nh8Dzk8"},
        {"nama": "Pantai Bentar", "link": "https://maps.app.goo.gl/qTk9GdjWydS8YFkeA"}
    ],
    "Sampang": [
        {"nama": "Air Terjun Toroan", "link": "https://maps.app.goo.gl/wCUnM2LK9eG6kcXq7"},
        {"nama": "Pantai Camplong", "link": "https://maps.app.goo.gl/VuZbvjfTEmETP3em6"},
        {"nama": "Hutan Kera Nepa", "link": "https://maps.app.goo.gl/Sn7bD9RtM3n9McYJ9"},
        {"nama": "Bukit Masegit", "link": "https://maps.app.goo.gl/Yn1DzUwbd6B1Fst99"}
    ],
    "Sidoarjo": [
        {"nama": "Lumpur Lapindo", "link": "https://maps.app.goo.gl/V4NV8igrFqsTPAvp7"},
        {"nama": "Monumen Jayandaru", "link": "https://maps.app.goo.gl/VQuyY9fHqyd9C5hd6"},
        {"nama": "Museum Mpu Tantular", "link": "https://maps.app.goo.gl/yMeu9hDT3qXmt89n9"},
        {"nama": "Candi Pari", "link": "https://maps.app.goo.gl/xYRi6Dn9bqLNgK3v5"}
    ],
    "Situbondo": [
        {"nama": "Savana Bekol", "link": "https://maps.app.goo.gl/5V5JLEm5gXZ2rjY9A"},
        {"nama": "Pantai Bama", "link": "https://maps.app.goo.gl/k11CJg67UH5bbB9C7"},
        {"nama": "Pantai Sejile", "link": "https://maps.app.goo.gl/GQWP8w8VQX5CwVUU6"},
        {"nama": "Kampung Kerapu", "link": "https://maps.app.goo.gl/p69BeHaGTDw4WP3R6"}
    ],
    "Sumenep": [
        {"nama": "Pantai Lombang", "link": "https://maps.app.goo.gl/21mBEqxGnJA53U1r6"},
        {"nama": "Gili Iyang", "link": "https://maps.app.goo.gl/vR6brydeQGq2emF18"},
        {"nama": "Gili Labak", "link": "https://maps.app.goo.gl/b8mPYKZ1WMtTfvJN7"},
        {"nama": "Museum Keraton Sumenep", "link": "https://maps.app.goo.gl/VNry2fiFk5rySD9U9"}
    ],
    "Trenggalek": [
        {"nama": "Pantai Prigi", "link": "https://maps.app.goo.gl/6xtm4BKucs6Bonr67"},
        {"nama": "Pantai Karanggoso", "link": "https://maps.app.goo.gl/ZJj8XttZZQRnNmke7"},
        {"nama": "Goa Lowo", "link": "https://maps.app.goo.gl/4ccaTpX1U7wTkLvX6"},
        {"nama": "Bukit Banyon", "link": "https://maps.app.goo.gl/nVsvuQTfYgndFLvc7"}
    ],
    "Tuban": [
        {"nama": "Air Terjun Putri Nglirip", "link": "https://maps.app.goo.gl/zHSH8hSKY6S9KaLe8"},
        {"nama": "Goa Akbar", "link": "https://maps.app.goo.gl/MUPV9T864oeBf9Rv7"},
        {"nama": "Pantai Boom", "link": "https://maps.app.goo.gl/dHKQqLHTHswXudvr5"},
        {"nama": "Goa Ngerong", "link": "https://maps.app.goo.gl/YicHuFQyeQwG4USK9"}
    ],
    "Tulungagung": [
        {"nama": "Pantai Gemah", "link": "https://maps.app.goo.gl/ke7Y5uc1WJ7uJw4Q7"},
        {"nama": "Pantai Sine", "link": "https://maps.app.goo.gl/9kvJ4GjJz67QgGCYA"},
        {"nama": "Air Terjun Lawean", "link": "https://maps.app.goo.gl/PwutS3RK1ZqwDSL57"},
        {"nama": "Pantai Kedung Tumpang", "link": "https://maps.app.goo.gl/T34woiwiumYpG1A18"}
    ],
    "Batu": [
        {"nama": "Jatim Park 1", "link": "https://maps.app.goo.gl/U9QLkfcwkRgTFKBg8"},
        {"nama": "Jatim Park 2", "link": "https://maps.app.goo.gl/2rMa7zAEuuaxA6LG7"},
        {"nama": "Museum Angkut", "link": "https://maps.app.goo.gl/przsanY7FbkUoNGU7"},
        {"nama": "Alun-Alun Batu", "link": "https://maps.app.goo.gl/YRZYp8R1bU2eiYtQ8"}
    ],
    "Surabaya": [
        {"nama": "Taman Bungkul", "link": "https://maps.app.goo.gl/jWtrWJvjq4nQJMF6A"},
        {"nama": "Monumen Tugu Pahlawan dan Museum Sepuluh Nopember Surabaya", "link": "https://maps.app.goo.gl/ZZmwVwC94PkQrz8R7"},
        {"nama": "Monumen Kapal Selam", "link": "https://maps.app.goo.gl/EJRoBfjqhdfBqu2EA"},
        {"nama": "Kebun Binatang Surabaya", "link": "https://maps.app.goo.gl/5aec7BHjf8WVFYni7"}
    ]
}

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, color=Color.WHITE, delay=0.03):
    """Efek mengetik dengan warna"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Color.RESET)

def print_banner():
    """Menampilkan banner dengan warna gradasi"""
    banner = f"""
{Color.CYAN}    ╔══════════════════════════════════════════════════════════════╗
{Color.BRIGHT_CYAN}    ║                                                              ║
{Color.BRIGHT_BLUE}    ║        🌴 SISTEM INFORMASI WISATA JAWA TIMUR 🌴              ║
{Color.BRIGHT_CYAN}    ║                                                              ║
{Color.CYAN}    ║            Jelajahi Keindahan Jawa Timur                     ║
{Color.BRIGHT_CYAN}    ║                                                              ║
{Color.CYAN}    ╚══════════════════════════════════════════════════════════════╝{Color.RESET}
    """
    print(banner)
    time.sleep(0.5)

def print_header(text, color=Color.YELLOW):
    """Menampilkan header dengan format yang menarik dan berwarna"""
    print(f"\n{color}╔{'═'*58}╗")
    print(f"║{text.center(58)}║")
    print(f"╚{'═'*58}╝{Color.RESET}\n")

def print_divider(char="─", color=Color.CYAN):
    """Menampilkan garis pembatas berwarna"""
    print(f"{color}{char*60}{Color.RESET}")

def loading_animation(text="Memuat", duration=1):
    """Animasi loading"""
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Color.CYAN}{animation[i % len(animation)]} {text}...{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " "*50 + "\r")

def pause():
    """Jeda untuk membaca informasi"""
    print(f"{Color.YELLOW}\n⏸  Tekan ENTER untuk melanjutkan...{Color.RESET}", end="")
    input()

def menu_utama():
    """Menampilkan menu utama dengan warna"""
    clear_screen()
    print_banner()
    
    print(f"{Color.BRIGHT_GREEN}1. 📖 Tata Cara Penggunaan{Color.RESET}")
    print(f"{Color.BRIGHT_BLUE}2. ℹ️  Penjelasan Singkat Program{Color.RESET}")
    print(f"{Color.BRIGHT_MAGENTA}3. 🗺️  Cari Tempat Wisata{Color.RESET}")
    print(f"{Color.BRIGHT_RED}4. 🚪 Keluar{Color.RESET}")
    
    print_divider()

def tata_cara():
    """Menampilkan tata cara penggunaan dengan warna"""
    clear_screen()
    loading_animation("Membuka panduan")
    print_header("TATA CARA PENGGUNAAN", Color.BRIGHT_GREEN)
    
    print(f"{Color.CYAN}Cara menggunakan program ini:\n{Color.RESET}")
    
    steps = [
        ("1", "Pilih menu yang tersedia dengan memasukkan nomor menu (1-4)"),
        ("2", f"Untuk mencari tempat wisata:\n   • Pilih menu nomor 3\n   • Pilih metode pencarian:\n     - Lihat Daftar: Browse semua daerah yang tersedia\n     - Search: Ketik langsung nama daerah yang dicari"),
        ("3", f"Cara menggunakan fitur Search:\n   • Format penulisan: Huruf pertama KAPITAL\n   • Contoh BENAR: {Color.GREEN}Malang, Surabaya, Banyuwangi{Color.WHITE}"),
        ("4", "Anda dapat kembali ke menu sebelumnya kapan saja"),
        ("5", "Untuk keluar dari program, pilih menu nomor 4")
    ]
    
    for num, text in steps:
        print(f"{Color.YELLOW}{num}.{Color.RESET} {Color.WHITE}{text}{Color.RESET}\n")
    
    print(f"\n{Color.BRIGHT_CYAN}💡 Tips:{Color.RESET}")
    tips = [
        "• Pastikan memasukkan nomor menu dengan benar",
        "• Perhatikan format penulisan saat menggunakan search",
        "• Jika tidak yakin dengan nama daerah, gunakan opsi 'Lihat Daftar'"
    ]
    for tip in tips:
        print(f"  {Color.CYAN}{tip}{Color.RESET}")
    
    pause()

def penjelasan_program():
    """Menampilkan penjelasan program dengan warna"""
    clear_screen()
    loading_animation("Memuat informasi")
    print_header("PENJELASAN SINGKAT PROGRAM", Color.BRIGHT_BLUE)
    
    print(f"{Color.CYAN}Program Sistem Informasi Wisata Jawa Timur{Color.RESET}\n")
    print(f"{Color.WHITE}Program ini dibuat untuk membantu wisatawan atau siapa saja yang ingin")
    print(f"mencari informasi tentang tempat wisata di Jawa Timur.{Color.RESET}\n")
    
    print(f"{Color.YELLOW}✨ Fitur Program:{Color.RESET}")
    features = [
        "• Database lengkap 32 daerah di Jawa Timur",
        "• Informasi tempat wisata populer di setiap daerah",
        "• Interface CLI yang mudah digunakan",
        "• Navigasi yang sederhana dan intuitif"
    ]
    for feature in features:
        print(f"  {Color.GREEN}{feature}{Color.RESET}")
    
    print(f"\n{Color.YELLOW}🎯 Tujuan:{Color.RESET}")
    print(f"  {Color.WHITE}Mempromosikan pariwisata Jawa Timur dan memudahkan masyarakat")
    print(f"  dalam merencanakan perjalanan wisata mereka.{Color.RESET}\n")
    
    print(f"{Color.YELLOW}📊 Data yang tersedia:{Color.RESET}")
    data_types = [
        "• Wisata alam (gunung, pantai, air terjun)",
        "• Wisata budaya (candi, museum, makam)",
        "• Wisata modern (taman hiburan, waterpark)"
    ]
    for data in data_types:
        print(f"  {Color.BRIGHT_CYAN}{data}{Color.RESET}")
    
    pause()

def pilih_daerah():
    """Menampilkan pilihan untuk browse atau search daerah"""
    while True:
        clear_screen()
        print_header("PILIH METODE PENCARIAN", Color.BRIGHT_MAGENTA)
        
        print(f"{Color.BRIGHT_GREEN}1. 📋 Lihat Daftar Semua Daerah{Color.RESET}")
        print(f"{Color.BRIGHT_BLUE}2. 🔍 Cari Daerah (Search){Color.RESET}")
        print(f"{Color.BRIGHT_YELLOW}3. ⬅️  Kembali ke Menu Utama{Color.RESET}")
        
        print_divider()
        
        pilihan = input(f"{Color.CYAN}Masukkan pilihan (1-3): {Color.RESET}").strip()
        
        if pilihan == "1":
            browse_daerah()
        elif pilihan == "2":
            search_daerah()
        elif pilihan == "3":
            break
        else:
            print(f"\n{Color.RED}❌ Pilihan tidak valid! Silakan pilih 1-3.{Color.RESET}")
            time.sleep(2)

def browse_daerah():
    """Menampilkan daftar semua daerah di Jawa Timur"""
    daerah_list = sorted(WISATA_JATIM.keys())
    
    while True:
        clear_screen()
        loading_animation("Memuat daftar daerah")
        print_header("DAFTAR DAERAH DI JAWA TIMUR", Color.BRIGHT_CYAN)
        print(f"{Color.YELLOW}Pilih daerah yang ingin Anda cari tempat wisatanya:{Color.RESET}\n")
        
        # Menampilkan dengan warna bergantian
        colors = [Color.BRIGHT_GREEN, Color.BRIGHT_CYAN]
        for idx, daerah in enumerate(daerah_list, 1):
            color = colors[idx % 2]
            print(f"{color}{idx:2d}. {daerah}{Color.RESET}")
        
        print(f"{Color.BRIGHT_YELLOW}{len(daerah_list) + 1:2d}. ⬅️  Kembali{Color.RESET}")
        print_divider()
        
        pilihan = input(f"{Color.CYAN}Masukkan pilihan (1-{len(daerah_list) + 1}): {Color.RESET}").strip()
        
        try:
            pilihan_int = int(pilihan)
            if 1 <= pilihan_int <= len(daerah_list):
                loading_animation(f"Membuka data {daerah_list[pilihan_int - 1]}")
                tampilkan_wisata(daerah_list[pilihan_int - 1])
            elif pilihan_int == len(daerah_list) + 1:
                break
            else:
                print(f"\n{Color.RED}❌ Nomor tidak valid!{Color.RESET}")
                time.sleep(2)
        except ValueError:
            print(f"\n{Color.RED}❌ Masukkan nomor yang valid!{Color.RESET}")
            time.sleep(2)

def search_daerah():
    """Mencari daerah dengan input nama"""
    while True:
        clear_screen()
        print_header("PENCARIAN DAERAH", Color.BRIGHT_BLUE)
        print(f"{Color.YELLOW}Format penulisan: Huruf pertama KAPITAL{Color.RESET}")
        print(f"{Color.GREEN}Contoh: Malang, Surabaya, Banyuwangi{Color.RESET}")
        print(f"\n{Color.BRIGHT_YELLOW}Ketik '0' untuk kembali{Color.RESET}\n")
        print_divider()
        
        nama_daerah = input(f"\n{Color.CYAN}🔍 Masukkan nama daerah: {Color.RESET}").strip()
        
        if nama_daerah == "0":
            break
        
        if not nama_daerah:
            print(f"\n{Color.RED}❌ Nama daerah tidak boleh kosong!{Color.RESET}")
            time.sleep(2)
            continue
        
        if not nama_daerah[0].isupper():
            print(f"\n{Color.RED}❌ Format salah! Huruf pertama harus KAPITAL.{Color.RESET}")
            print(f"{Color.YELLOW}   Contoh yang benar: Malang, Surabaya, Batu{Color.RESET}")
            time.sleep(3)
            continue
        
        # Animasi pencarian
        loading_animation(f"Mencari {nama_daerah}")
        
        if nama_daerah in WISATA_JATIM:
            print(f"{Color.GREEN}✅ Daerah ditemukan!{Color.RESET}")
            time.sleep(1)
            tampilkan_wisata(nama_daerah)
        else:
            print(f"\n{Color.RED}❌ Daerah '{nama_daerah}' tidak ditemukan!{Color.RESET}")
            print(f"\n{Color.YELLOW}💡 Daftar daerah yang tersedia:{Color.RESET}")
            daerah_list = sorted(WISATA_JATIM.keys())
            for i in range(0, len(daerah_list), 4):
                line = ", ".join(daerah_list[i:i+4])
                print(f"{Color.BRIGHT_CYAN}   {line}{Color.RESET}")
            pause()

def tampilkan_wisata(daerah):
    """Menampilkan daftar wisata di daerah terpilih"""
    while True:
        clear_screen()
        print_header(f"TEMPAT WISATA DI {daerah.upper()}", Color.BRIGHT_MAGENTA)
        
        wisata_list = WISATA_JATIM[daerah]
        
        if wisata_list:
            colors = [Color.BRIGHT_GREEN, Color.BRIGHT_CYAN, Color.BRIGHT_YELLOW, Color.BRIGHT_MAGENTA]
            for idx, wisata in enumerate(wisata_list, 1):
                color = colors[idx % len(colors)]
                print(f"{color}{idx:2d}. 🏖️  {wisata['nama']}{Color.RESET}")
            
            print(f"\n{Color.YELLOW}📍 Total: {len(wisata_list)} tempat wisata{Color.RESET}")
            print_divider()
            
            print(f"\n{Color.CYAN}Pilihan:{Color.RESET}")
            print(f"{Color.BRIGHT_GREEN}1. 🔗 Lihat link Google Maps{Color.RESET}")
            print(f"{Color.BRIGHT_YELLOW}2. ⬅️  Kembali{Color.RESET}")
            
            pilihan = input(f"\n{Color.CYAN}Masukkan pilihan (1-2): {Color.RESET}").strip()
            
            if pilihan == "1":
                clear_screen()
                loading_animation("Memuat link Google Maps")
                print_header(f"LINK GOOGLE MAPS - {daerah.upper()}", Color.BRIGHT_BLUE)
                for idx, wisata in enumerate(wisata_list, 1):
                    print(f"\n{Color.YELLOW}{idx:2d}. {wisata['nama']}{Color.RESET}")
                    print(f"    {Color.BRIGHT_BLUE}🔗 {wisata['link']}{Color.RESET}")
                print_divider()
                print(f"\n{Color.BRIGHT_CYAN}💡 Copy link di atas dan paste di browser Anda{Color.RESET}")
                pause()
            elif pilihan == "2":
                break
            else:
                print(f"\n{Color.RED}❌ Pilihan tidak valid!{Color.RESET}")
                time.sleep(1)
        else:
            print(f"{Color.YELLOW}Belum ada data wisata untuk daerah ini.{Color.RESET}")
            print_divider()
            pause()
            break

def goodbye_animation():
    """Animasi perpisahan"""
    clear_screen()
    print_header("TERIMA KASIH", Color.BRIGHT_GREEN)
    
    messages = [
        "   Terima kasih telah menggunakan",
        "   Sistem Informasi Wisata Jawa Timur!",
        "",
        "   Selamat berwisata! 🌴✨"
    ]
    
    for msg in messages:
        typing_effect(msg, Color.CYAN, 0.05)
    
    print(f"\n{Color.YELLOW}{'='*60}{Color.RESET}\n")
    time.sleep(1)

def main():
    """Fungsi utama program"""
    while True:
        menu_utama()
        pilihan = input(f"{Color.CYAN}Masukkan pilihan menu (1-4): {Color.RESET}").strip()
        
        if pilihan == "1":
            tata_cara()
        elif pilihan == "2":
            penjelasan_program()
        elif pilihan == "3":
            pilih_daerah()
        elif pilihan == "4":
            goodbye_animation()
            break
        else:
            print(f"\n{Color.RED}❌ Pilihan tidak valid! Silakan pilih menu 1-4.{Color.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()
