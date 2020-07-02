import requests
import sys
from bs4 import BeautifulSoup as bs
import pytesseract
from PIL import Image
import PIL.ImageOps
from lxml import html 

def cli():
    print('testing..')
    print('enter dl no. : ',end="") 
    dl=input()
    print('enter dob. in a format:- DD-MM-YYYY :  ',end="")
    dob=input()
    #get_captcha()
    #cap=get_captcha()
    cap='bm28y'
    print('entering CAPTCHA... : ',cap)
        
   # print('press 1 to fetch or 0 to reset :  ',end="")
   # res=input()
    post(dl,dob,cap)
       
    
            
def post(dl,dob,cap):
    url='https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
    r=requests.get(url)
    payload = {
    'form_rcdl:tf_dlNO': dl,
    'form_rcdl:tf_dob_input': dob,
    'form_rcdl:j_idt32:CaptchaID':cap,
    'ui-button-text ui-c': 'Check Status'
    }
    r=requests.post(url,data=payload)
    print(dl,dob,cap)
    
def fetch():
    '''url='https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
    # path = '//*[@id="form_rcdl:j_idt124"]/table[1]/tbody/tr[2]'
    r=requests.get(url)
    tree = html.fromstring(r.content)
    Word = tree.xpath('//*[@id="form_rcdl"]/div[1]/div[3]/div[2]/div/ul/li[1]')[0].text
    print (Word)'''
    
    # url to scrape data from 
    link = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
  
    path = '//*[@id="form_rcdl:j_idt45"]/div/div[2]/span'
  
    response = requests.get(link) 
    byte_string = response.content  
    source_code = html.fromstring(byte_string) 
    tree = source_code.xpath(path) 
    print(tree[0].text_content()) 

     
     
#fetch and print in json

def get_captcha():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\abhis\Desktop\tesseract'
    image = Image.open('image3.jpg').convert('RGB')
    text=pytesseract.image_to_string(image)
    return text
    
if __name__ == '__main__':
    cli()
    fetch()
    print("success")


#<img id="form_rcdl:j_idt32:j_idt38" src="/rcdlstatus/DispplayCaptcha?txtp_cd=1&amp;bkgp_cd=2&amp;noise_cd=2&amp;gimp_cd=3&amp;txtp_length=5&amp;pfdrid_c=true?1669730776&amp;pfdrid_c=true" alt="">