import math

def hitung_silinder(jari_jari, tinggi):
    """
    Menghitung keliling alas, luas permukaan, dan volume silinder.
    """
    # Keliling alas silinder berbentuk lingkaran
    keliling = 2 * math.pi * jari_jari
    
    # Luas permukaan silinder = 2 × π × r × (r + t)
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    
    # Volume silinder = π × r² × t
    volume = math.pi * (jari_jari ** 2) * tinggi
    
    return keliling, luas_permukaan, volume

def hitung_kerucut(jari_jari, tinggi):
    """
    Menghitung keliling alas, luas permukaan, dan volume kerucut.
    """
    # Keliling alas kerucut berbentuk lingkaran
    keliling = 2 * math.pi * jari_jari
    
    # Menghitung garis pelukis (s) menggunakan teorema Phytagoras: s = √(r² + t²)
    garis_pelukis = math.sqrt((jari_jari ** 2) + (tinggi ** 2))
    
    # Luas permukaan kerucut = π × r × (r + s)
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    
    # Volume kerucut = 1/3 × π × r² × t
    volume = (1 / 3) * math.pi * (jari_jari ** 2) * tinggi
    
    return keliling, luas_permukaan, volume

def main():
    print("=== Program Dimensi Silinder dan Kerucut ===")
    
    try:
        # 1. Input: Meminta nilai dari user untuk silinder
        print("\n[ SILINDER ]")
        r_silinder = float(input("Masukkan jari-jari silinder: "))
        t_silinder = float(input("Masukkan tinggi silinder: "))
        
        # 1. Input: Meminta nilai dari user untuk kerucut
        print("\n[ KERUCUT ]")
        r_kerucut = float(input("Masukkan jari-jari kerucut: "))
        t_kerucut = float(input("Masukkan tinggi kerucut: "))
        
        # 2. Function: Memanggil fungsi yang telah dibentuk
        keliling_silinder, luas_silinder, volume_silinder = hitung_silinder(r_silinder, t_silinder)
        keliling_kerucut, luas_kerucut, volume_kerucut = hitung_kerucut(r_kerucut, t_kerucut)
        
        # 3. Output: Menampilkan hasil perhitungan silinder
        print("\n=== HASIL PERHITUNGAN SILINDER ===")
        print(f"Keliling Alas  : {keliling_silinder:.2f}")
        print(f"Luas Permukaan : {luas_silinder:.2f}")
        print(f"Volume         : {volume_silinder:.2f}")
        
        # 3. Output: Menampilkan hasil perhitungan kerucut
        print("\n=== HASIL PERHITUNGAN KERUCUT ===")
        print(f"Keliling Alas  : {keliling_kerucut:.2f}")
        print(f"Luas Permukaan : {luas_kerucut:.2f}")
        print(f"Volume         : {volume_kerucut:.2f}")
        
    except ValueError:
        print("\n[Error!] Masukkan harus berupa angka yang valid.")

if __name__ == "__main__":
    main()
