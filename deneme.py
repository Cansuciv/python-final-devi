yetki=input(print("Sisteme admin olarak giriş yapmak istiyorsanız 'a'ya basınız, kullanıcı olarak giriş yapmak istiyorsanız 'k'ye basınız:"))
if yetki.lower()=='a':
    #kullanıcı adını girerek kullanıcının ad soyad,tel no, tc no, adres, eposta gibi bilgilerine  ulaşmak
    print("-ADMİN GİRİŞİ-")
    user_name=input(print("Kullanıcı adını giriniz:"))
    print("Kullanıcının adı ve soyadı:")
    print("kullanıcının e-posta adresi:")
    print("Kullanıcının adresi:")
    print("Kullanıcının telefon numarası:")
    print("Kullanıcının tc numarası:")

else:
    print("-KULLANICI GİRİŞİ-")
    
    while True:
        print("1-Sisteme üye ol")
        print("2-Sisteme giriş yap")
        print("3-Şifremi unuttum")
        secim=int(input(print("Lütfen bir seçenek giriniz:")))
        
       
        #üye olma menüsü(ad-soay, tel no, tc no, adres , şifre girişi yapılır)
        if secim==1:
            print("-SİSTEME ÜYE OL-")
            ad_soyad=input(print("Adınızı ve soyadınızı giriniz:"))
            kullanici_adi=input(print("Kullanıcı adı giriniz:"))
            while True: #tel no da sadece rakam girişi yapma
                tel_no=input(print("Telefon numaranızı giriniz:"))
                if tel_no.isdecimal():
                    break
                else:
                    print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")
                    
            e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
            
            while True: #tc no da sadece rakam girişi yapma
                tc_no=input(print("TC numaranızı giriniz:"))
                if tc_no.isdecimal():
                    break
                else:
                    print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")
                    
            adres=input(print("Lütfen adresinizi giriniz:"))
            sifre=input(print("Lütfen bir şifre giriniz:"))
            print("\nSİSTEME ÜYE OLUNDU!!! \n\n")
            
            
        #tel no ya da eposta adresi ile sisteme giriş yapma
        elif secim==2:
            print("-SİSTEME GİRİŞ YAP-")
            giris_secim=input(print("Sisteme telefon numarası ile giriş yapmak için '7'ye, e-posta adresi ile giriş yapmak için '8'ye basınız:"))
            #tel no ile giriş yapma
            if giris_secim=="7":
                while True: #tel no da sadece rakam girişi yapma
                    tel_no=input(print("Telefon numaranızı giriniz:"))
                    if tel_no.isdecimal():
                        break 
                    else:
                        print("Hatalı giriş yaptınız. Lütfen sadece rakam giriniz.")

                sifre=input(print("Lütfen şifrenizi giriniz:"))
                print("\nSİSTEME GİRİŞ YAPILDI!!! \n\n")
                
            #eposta adresiyle giriş yapma
            elif giris_secim=="8":
                e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
                sifre=input(print("Lütfen şifrenizi giriniz:"))
                print("\nSİSTEME GİRİŞ YAPILDI!!! \n\n")
                
            else:
                print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")
                
            

        #şifremi unuttum ile tel no ya da eposta adresiyle şifer değiştirme
        elif secim==3:
            print("-ŞİFREMİ UNUTTUM-")
            sifremi_unuttum=input(print("Şifrenizi unuttunuz ve değiştirmek mi istiyorsunuz? Şİfrenizi telefon numarası ile değiştirmek için 4'e, e-posta adresi ile değiştirmek için 5'ye basınız:"))
            #tel no ile şifre değiştirme. telefona gelen kodu girerek yeni şifre oluşturma
            if sifremi_unuttum=="4":
                while True: #tel no da sadece rakam girişi yapma
                    tel_no=input(print("Telefon numaranızı giriniz:"))
                    if tel_no.isdecimal():
                        break
                    else:
                        print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")   
                
                kod=input(print("Telefonunuza gelen kodu giriniz:"))
                yeni_sifre=input(print("Yeni şifrenizi giriniz:"))
                print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                
            #eposta ile şifre değiştirme. epostaya gelen kodu girerek yeni şifre oluşturma
            elif sifremi_unuttum=="5":
                e_posta=input(print("Lütfen e-posta adresinizi giriniz:"))
                kod=input(print("E-posta adresinize gelen kodu giriniz:"))
                yeni_sifre=input(print("Yeni şifrenizi giriniz:"))
                print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                
            else:
                print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")
