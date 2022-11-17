"""
Servis 3
Treći servis sprema svaku aktivnost i tip u
temporary storage. Ukoliko se radi o ruti /otherActivities, za svaku
aktivnost šalje zahtjev na https://randomuser.me/api/ od kojeg uzme
ime, prezime i datum rođenja te pridoda ih kao nove ključeve aktivnosti.
"""