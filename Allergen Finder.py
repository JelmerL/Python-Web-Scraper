import requests
from bs4 import BeautifulSoup as bs
import re

print()
print("So you want to search for allergens on a website?")
print()
#input allergens
compounds = [x.lower() for x in [
    '2-Bromo-2-nitropropane-1,3-diol',
    '2-Nitro-2-bromo-1,3-propanediol',
    'Bronidiol',
    'Bronocot',
    'Bronopol',
    'Bronosol',
    'Bronotak'
    'HSDB 7195',
    'Lexgard bronopol',
    'NSC 141021',
    'Onyxide 500',
    'beta-Bromo-beta-nitrotrimethyleneglycol',
    'Germall',
    '2(3H)-Benzothiazolethione',
    '2-Benzothiazolethiol',
    '2-Benzothiazolinethione',
    '2-Benzothiazolyl mercaptan',
    '2-MBT',
    '2-Mercaptobenzothiazole',
    '2-Mercaptobenzthiazole',
    '2-Mercptobenzothiazole',
    'Accel M',
    'Accelerator M',
    'Benzothiazole',
    'mercapto',
    'Benzothiazole-2-thione',
    'Benzothiazolethiol',
    'Captax',
    'Dermacid',
    'Ekagom G',
    'Kaptaks',
    'Kaptax',
    'MBT',
    'Mebetizole',
    'Mebithizol',
    'Mercaptobenzothiazol',
    'Mercaptobenzothiazole',
    'Mercaptobenzothiazole (VAN)',
    'Mercaptobenzthiazole',
    'Mertax',
    'Nuodeb 84',
    'Nuodex 84',
    'Pennac MBT powder',
    'Pneumax MBT',
    'Rokon',
    'Rotax',
    'Royal MBT',
    'Soxinol M Sulfadene',
    'Thiotax',
    'USAF GY-3',
    'USAF XR-29',
    'Vulkacit M',
    'Vulkacit mercapto',
    'Vulkacit mercapto/C',
    '1,2-Dibromo-2,4-dicyanobutane',
    '1-Bromo-1-(bromomethyl)-1,3-propanedicarbonitrile',
    '2-Bromo-2-(bromomethyl)glutaronitrile 2-Bromo-2',
    'bromoethylglutaronitrile',
    'BBMG',
    'Bromothalonil',
    'Caswell No 114G',
    'EINECS 252-681-0',
    '252-681-0',
    '2526810',
    '111001',
    'HSDB 7313',
    'Metacide 38',
    'Methyldibromoglutaronitrile',
    'Pentanedinitrile,2-bromo-2-(bromomethyl)',
    'Tektamer',
    'Tektamer 38',
    'Tektamer 38AD',
    'Tuopai DM 01',
    'Neomycin sulfate',
    'Cortisporin',
    'Dexacidin',
    'Intromycin',
    'Neosone',
    'Neosporin',
    'Spectrocin',
    'Caswell No. 595A',
    '595A',
    'EINECS 215-773-1',
    '215-773-1',
    '2157731',
    'Fradiomycin sulfate',
    'Lidamycin creme',
    'Lidamycin',
    'Mycaifradin sulfate',
    'Mycifradin',
    'Mycigient',
    'Myciguent',
    'Neobiotic',
    'Neofracin',
    'Neomix',
    'Otobiotic',
    'USAF CB-19',
    'Tresaderm (Veterinary)',
    'Neobacimyx (Veterinary)',
    'Panolog Cream (Veterinary)',
    'Biosol (Veterinary)',
    '006313',
    'Potassiumdichromate',
    'Dipotassiumdichromate',
    'Bichromate',
    'Chromium compounds',
    'Chromium',
    'chromium salts',
    'Chromium metal',
    'chrome',
    'Chromic acid salts ',
    'N-(3-(Dimethylamino)propyl) octadecanamide',
    'Octadecanamide, N-(3-(dimethylamino)propyl)',
    'N,N-Dimethyl-3-octadecanoylaminopropylamine',
    'N,N-Dimethyl-N-(3-stearamidopropyl)amine',
    'N-(3-Dimethylaminopropyl) octadecamide',
    'Octadecanoylamidopropyl dimethylamine',
    'Stearic acid, 3-dimethylaminopropylamide',
    'Dimethylaminopropyl stearamide',
    'Stearamidopropyl dimethylamine',
    'Tegamine S 13',
    'EINECS 231-609-1',
    '231-609-1',
    '2316091',
    'Lexamine S 13',
    'NSC 86167',
    '86167',
    'fragrance'
    ]]

naturalname = [x.lower() for x in [
    'tansy',
    ]]

#input and compile pattern for CAS number matches
CAS = [x.lower() for x in[
    '52-51-7',
    '52517',
    '149304',
    '149-30-4',
    '35691-65-7',
    '35691657',
    '1405-10-3',
    '1405103',
    '7778-50-9',
    '7778509',
    '7651-02-07',
    '76510207'
    ]]

keylog = 'y'

#start a loop that keeps asking for URL input when necessary

while keylog == 'y':
    
    #Ask for URL input
    print("Input URL starting with HTTP:")
    try:
        url = input()
        print("Ok Scanning",url, "for Allergies")

        #Get page and convert to searchable lowercase string
        res = requests.get(url)
        html_page = res.content
        soup = bs(html_page, 'html.parser')
        page_soup = soup.find_all(text=True)
        page_TEXT = str(page_soup)
        page_text = page_TEXT.lower()

    #print the possible allergens and build lists for potential future use
        
        matchedcompounds = []
        matchedCAS = []
        matchednaturalname = []

        print()
        print("Compounds that are potential allergens found:")
        for i in compounds:
            if i in page_text:
                print('\t',"-",i.capitalize())
                matchedcompounds.append(i)
        if len(matchedcompounds)==0:
            print('\t',"GOOD NEWS, NONE FOUND!")
                
        print()
        print("CAS numbers that are potential allergens found:")
        for j in CAS:
            if j in page_text:
                print('\t',"-",j.capitalize())
                matchedCAS.append(j)
        if len(matchedCAS)==0:
            print('\t',"GOOD NEWS, NONE FOUND!")

        print()
        print("Natural or product names that are potential allergens found:")
        for x in naturalname:
            if x in page_text:
                print('\t',"-",x.capitalize())
                matchednaturalname.append(x)
        if len(matchednaturalname)==0:
            print('\t',"GOOD NEWS, NONE FOUND!")

        #Ask if you want to do another search and restart the loop or exit
        print()
        print("Pres y and enter to do another search and anything else to exit:")
        keylog = input()

    except:
        print()
        print("WHOOPS")
        print("Your URL is not correct, please restart and try again. Remember you need to provide the full URL including https://www. etc.")
        k = input("hit any key to try again")