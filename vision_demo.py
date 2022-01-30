from google.cloud import vision
import io
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keyFile.json"
def detect_text(path):
    """Detects text in the file."""
    ret = []
    client = vision.ImageAnnotatorClient()

    

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
   # print(texts)

    for text in texts:
     #   print(type(text))
      #  print('\n"{}"'.format(text.description))
   #     print('-----------------------------')
        ret = text.description.split()
        ret2 = text.description.split('\n')
   #     print(ret)
        break
    return ret, ret2





def find_invoice_num(lis):
    count =0 

    for i in range(len(lis)):
        key_word = lis[i]
        if key_word.lower()== "invoice" :
            count += 1
            if count > 1:
                key_word = lis[i+1]
                return key_word
    return "N/A"
    
def find_address(lis):
    
    for i in range(len(lis)):
        s = lis[i]
        if not is_int(s) or len(s) != 5:
            continue
        j = i-1
        while not is_int(lis[j]):
            j -= 1
        ret = ''
        while j <= i +2:
            ret += lis[j] + ' '
            j+=1
        if 'USA' in ret:
            return ret
        print('--------------')

def find_total(lis):
    max_value =0.0

    for i in range(len(lis)):
        if(is_float(lis[i])) and '.' in lis[i]:
            num_cost = float(lis[i])
            if(num_cost >max_value):
                max_value = num_cost
            
                

    return max_value


def item_names(lis):
    items = []
    spec_it = " "
    count = 1

    for i in range(len(lis)):
        if(is_int(lis[i]) or is_float(lis[i])):

            tmp = int(lis[i])
            if(tmp == count):
                count += 1






        #find number 
        ## go forwards  and find name 



        
def is_int(s):
    try:
        s = int(s)
        return True
    except:
        return False

        
def is_float(s):
    try:
        s = float(s)
        return True
    except:
        return False

s = (detect_text('advert_invoice.jpg'))

print(item_names(s[0]))
        

        
    
        


detect_text('advert_invoice.jpg')