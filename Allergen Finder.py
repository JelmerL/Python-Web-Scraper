import requests
from bs4 import BeautifulSoup as bs
import re

print()
print("So you want to search for allergens on a website?")
print()
#input compound names
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
    'beta-Bromo-beta-nitrotrimethyleneglycol Germall 11',
    'Germall 11',
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
    'Soxinol M',
    'stearate',
    'Sulfadene',
    'Thiotax',
    'USAF GY-3',
    'USAF XR-29',
    'Vulkacit M',
    'Vulkacit mercapto',
    'Vulkacit mercapto/C',
    'Methyldibromo Glutaronitrile',
    'MDBGN',
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
    'EPA Pesticide Chemical Code',
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
    'Tresaderm',
    'Neobacimyx (Veterinary)',
    'Neobacimyx',
    'Panolog Cream (Veterinary)',
    'Panolog Cream',
    'Biosol (Veterinary)',
    'Biosol',
    'EPA Pesticide Chemical Code 006313',
    '006313',
    'Potassium Dichromate',
    'Potassiumdichromate',
    'Dipotassiumdichromate',
    'Bichromate',
    'Chromium compounds',
    'Chromium',
    'chromium salts',
    'Chromium metal',
    'chrome',
    'Chromic acid salts ',
    'Amidoamine',
    'stearamidopropyl dimethylamine'
    'N-(3-(Dimethylamino)propyl) octadecanamide',
    'Octadecanamide, N-(3-(dimethylamino)propyl)',
    'Octadecanamide',
    'N,N-Dimethyl-3-octadecanoylaminopropylamine',
    'N,N-Dimethyl-N-(3-stearamidopropyl)amine',
    'N-(3-Dimethylaminopropyl) octadecamide',
    'Octadecanoylamidopropyl dimethylamine',
    'Stearic acid, 3-dimethylaminopropylamide',
    'Stearic acid',
    'Dimethylaminopropyl stearamide',
    'Stearamidopropyl dimethylamine',
    'Tegamine S 13',
    'EINECS 231-609-1',
    '231-609-1',
    '2316091',
    'Lexamine S 13',
    'NSC 86167',
    '86167',
    ]]

#input questionable allergens
questionable = [x.lower() for x in [
    'sesquiterpene lactone mix',
    'sesquiterpene lactone',
    'composite',
    'asteraceae',
    'Alantolactone',
    'EINECS 208-899-3',
    '208-899-3',
    '2088993',
    'CAS RN:546-43-0',
    '546-43-0',
    '546430',
    'Costunolide',
    'sesquiterpene',
    'Costus Lactone',
    'Dehydrocostunolide',
    'Dehydrocostus Lactone',
    'CAS RN:553-21-9',
    'CAS 553219',
    '553219',
    'CAS RN: 477-43-0',
    'CAS 477-43-0',
    '477430',
    'NA57',
    'arnica',
    'bitterweed',
    'broomweed',
    'capeweed',
    'champaca of perfumery',
    'Chrysanthemum',
    'cosmos',
    'cotton thistle',
    'feverfew',
    'fleabane',
    'hampweed',
    'laurel',
    'lettuce',
    'margeurite',
    'marsh elder',
    'oxeye',
    'pyrethrum',
    'sagebrush',
    'sow thistle',
    'stinkwort',
    'tansy',
    'whitewood of commerce',
    'artichoke',
    'boneset',
    'burdock',
    'chamomile',
    'CHAMOMILLA',
    'chicory',
    'Calendula',
    'cocklebur',
    'costus of perfumery',
    'encelia',
    'fireweed',
    'gayule',
    'ironweed',
    'leafcup',
    'liverwort',
    'marigold',
    'mugwort',
    'parthenium',
    'ragweed',
    'sneezeweed',
    'star thistle',
    'tulip tree',
    'wormwood',
    'yarrow',
    'NA70',
    'Fragrance Mix II',
    'Coumarin',
    'Lyral',
    'Citronellol',
    'Farnesol',
    'Citral',
    'a-Hexylcin-namicaldehyde',
    'fragrance',
    'fragrance-free',
    'parfum',
    'Coumarin',
    '2H-1-Benzopyran-2-one',
    'Coumarin [NF X]',
    'Tonka bean camphor',
    '1,2-Benzopyrone',
    '2-Oxo-1,2-benzopyran',
    '2-Propenoic acid, 3-(2-hydroxyphenyl)-, delta-lactone',
    '2-Propenoic acid',
    '3-(2-hydroxyphenyl)',
    'delta-lactone',
    'delta lactone',
    '2-Propenoic acid, 3-(2-hydroxyphenyl)-delta-lactone',
    '2H-1-Benzopyran, 2-oxo-',
    '2H-1-Benzopyran, 2-oxo',
    'Benzopyran',
    '2H-1-Benzopyran-2-one',
    '2H-Benzo(b)pyran-2-one',
    '3-(2-Hydroxyphenyl)-2-propenoic delta-lactone',
    '5,6-Benzo-alpha-pyrone',
    '5-17-10-00143 (Beilstein Handbook Reference)',
    '5-17-10-00143',
    '5171000143',
    'Al3-00753',
    'BRN 0383644',
    'Benzo-alpha-pyrone',
    'CCRIS 181',
    'Caswell No. 259C',
    'Caswell 259C',
    '259C',
    'Cinnamic acid, o-hydroxy-, delta-lactone',
    'Coumarin',
    'Coumarinic anhydride',
    'Coumarinic lactone',
    'Cumarin',
    'EINECS 202-086-7',
    '202-086-7',
    '2020867',
    'EPA Pesticide Chemical Code 127301',
    '127301',
    'Rattex',
    'Cis-o-Coumaric acid anhydride',
    'cis-o-Coumarinic acid lactone',
    '0-Coumaric acid lactone',
    '0-Hydroxycinnamic acid lactone',
    '0-Hydroxycinnamic lactone',
    'Lyral',
    '4-(4-Hydroxy-4-methylpentyl)-3-cyclohexene-1-carboxaldehyde',
    'BRN 2046455',
    '2046455',
    'EINECS 250-863-4',
    '250-863-4',
    '3-Cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)-',
    '3-Cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)',
    '3-Cyclohexene-1-carboxaldehyde',
    '4-(4-hydroxy-4-methylpentyl)-',
    '4-(4-hydroxy-4-methylpentyl)',
    '4-(4-Hydroxy-4-methylpentyl)cyclohex-3-enecarbaldehyde',
    'cyclohex-3-enecarbaldehyde',
    '3-Cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)-',
    '3-Cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)',
    'Citronellol',
    '2,6-Dimethyl-2-octen-8-01',
    '3,7-Dimethyl-6-octen-1-ol',
    '4-01-00-02188 (Beilstein Handbook Reference)',
    '4-01-00-02188',
    'A13-25080',
    'BRN 1721507',
    '1721507',
    'CCRIS 7452',
    '7452',
    'Cephrol',
    'Citronellol',
    'Java citronella oil',
    'citronella',
    'EINECS 203-375-0',
    '203-375-0',
    'Elenol',
    'FEMA No. 2309',
    'NSC 8779',
    'Rhodinol',
    'Rodinol',
    'Farnesol',
    '2,6,10-Dodecatrien-1-ol, 3,7,11-trimethyl-',
    '2,6,10-Dodecatrien-1-ol, 3,7,11-trimethyl',
    '3,7,11-Trimethyl-2,6,10-dodecatrienol',
    '3,7,11-Trimethyl-2,6,10-dodecatrien-1-ol',
    'Trimethyl dodecatrienol',
    'NA89',
    'Amerchol L101',
    'amerchol',
    'CAS# 8029-05-8',
    '8029-05-8',
    '8029058',
    'Amerchol L-101',
    'Amerchol L101',
    'EE347',
    'Butylhydroxytoluene (BHT)',
    'Butylhydroxytoluene',
    'BHT',
    'CAS#: 128-37-0',
    '128370',
    '128-37-0',
    'lonol',
    'lonol CP-antioxidant',
    '1-Hydroxy-4-methyl-2,6-di-tert-butylbenzene',
    'AOX 4K',
    '2,6-Bis(1,1-dimethylethyl)-4-methylphenol',
    'Advastab 401',
    '2,6-Di-t-butyl-4-methylphenol',
    'Agidol',
    '2,6-Di-t-butyl-p-cresol',
    'Agidol 1',
    '2,6-Di-terc.butyl-p-kresol',
    'Alkofen BP',
    '2,6-Di-terc.butyl-p-kresol (Czech)',
    '2,6-Di-terc.butyl-p-kresol',
    'Antioxidant 264',
    '2,6-Di-tert-butyl-1-hydroxy-4-methylbenzene',
    'Antioxidant 29',
    '2,6-Di-tert-butyl-4-сresol',
    'Antioxidant 30',
    '2,6-Di-tert-butyl-4-hydroxytoluene',
    'Antioxidant 4',
    '2,6-Di-tert-butyl-4-methylhydroxybenzene',
    'Antioxidant 4K',
    '2,6-Di-tert-butyl-4-methylphenol',
    'Antioxidant DBPC',
    '2,6-Di-tert-butyl-p-cresol',
    'Antioxidant KB',
    '2,6-Di-tert-butyl-p-methylphenol',
    'Antioxidant MPJ',
    '3,5-Di-tert-butyl-4-hydroxytoluene',
    'Antioxidant T 501',
    '4-Hydroxy-3,5-di-tert-butyltoluene',
    'Antox QT',
    '4-Methyl-2,6-di-terc. Butylfenol',
    'Butylfenol',
    'Antrancine 8',
    '4-Methyl-2,6-di-terc. butylfenol (Czech)',
    '4-Methyl-2,6-di-terc. butylfenol',
    'BAT',
    '4-Methyl-2,6-di-tert-butylphenol',
    'BHT',
    '4-Methyl-2,6-tert-butylphenol',
    'A13-19683',
    'BHT 264',
    'AO 29',
    'BUKS',
    'AO 4',
    'Butylated hydroxytoluene',
    'AO 4K',
    'Butylated hydroxytoluol',
    'AOX 4',
    'Butylhydroxytoluene',
    'Butylohydroksytoluenu'
    'Butylohydroksytoluenu [Polish]',
    'CAO 1',
    'CAO 3',
    'CCRIS 103',
    'Caswell No. 291A',
    '291A',
    'Catalin antioxydant 1',
    'Catalin cao-3',
    'Chemanox 11',
    'DBPC',
    'DBPC (technical grade)',
    'Dalpac',
    'Deenax',
    'Di-tert-butyl-p-cresol',
    'Di-tert-butyl-p-cresol (VAN)',
    'Di-tert-butyl-p-methylphenol',
    'Dibunol',
    'Dibutylated hydroxytoluene',
    'EINECS 204-881-4',
    '204-881-4',
    'EPA Pesticide Chemical Code 022105',
    '022105',
    'FEMA No. 2184',
    '2184',
    'HSDB 1147',
    'Impruvol',
    'lonol',
    'lonol (antioxidant)',
    'Ionol 1',
    'Ionol CP',
    'Ionole',
    'Kerabit',
    'NCI-C03598',
    'NSC 6347',
    'Nocrac 200',
    'Nonox TBC',
    'P 21',
    'P21',
    'Parabar 441',
    'Paranox 441',
    'Phenol, 2,6-bis(1,1-dimethylethyl)-4-methyl-',
    'Phenol, 2,6-bis(1,1-dimethylethyl)-4-methyl',
    'Stavox',
    'Sumilizer BHT',
    'Sustane',
    'Sustane BHT',
    'Swanox BHT',
    'Tenamen 3',
    'Tenamene 3',
    'Tenox BHT',
    'Tonarol',
    'Topanol',
    'Topanol 0',    
    'Topanol O',
    'Topanol OC',
    'Toxolan P',
    'Vanlube PC',
    'Vanlube PCX',
    'Vianol',
    'Vulkanox KB',
    '0-Di-tert-butyl-p-methylphenol'
]]

#input natural names for matches
naturalname = [x.lower() for x in [
    'tansy',
    'Tanacetum vulgare',
    'Tanacetum annuum',
    'Laurus nobilis',
    'Chrysanthemum morifolium',
    'Cynara scolymus',
    'Arctium',
    'Matricaria chamomilla',
    'Tagetes',
    'Helianthus annuus',
    'Helianthus',
    ]]

#input CAS number matches
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
    '114G',
    '76510207'
    ]]

#input NA number matches
na = [x.lower() for x in [
    'NA54',
    'NA51',
    'ST165',
    'ST177',
    'NA05',
    'NA03',
    'NA10'
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
        matchedna = []
        matchedquestionable = []

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
            
        print()
        print("NA codes that are potential allergens found:")
        for x in na:
            if x in page_text:
                print('\t',"-",x.capitalize())
                matchedna.append(x)
        if len(matchedna)==0:
            print('\t',"GOOD NEWS, NONE FOUND!")

        print()
        print("Questionable names that are potential allergens found:")
        for x in questionable:
            if x in page_text:
                print('\t',"-",x.capitalize())
                matchedquestionable.append(x)
                if x.lower() == "fragrance-free":
                    print("!! Looks like they're advertising fragrance-free somewhere on the page !!")
        if len(matchedquestionable)==0:
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