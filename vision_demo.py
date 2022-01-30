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
   # print('Texts:')
    #print(texts)

    for text in texts:
     #   print(type(text))
      #  print('\n"{}"'.format(text.description))
   #     print('-----------------------------')
        ret = text.description.split()
        ret2 = text.description.split('\n')
      #  print(ret2)
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
    #print(lis)
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
            if lis[j] == 'USA':
                break
            j+=1
        return ret
        print('--------------')
#[(name1,qty1),(name2,qty2)]

def find_total(lis):
    max_value =0.0

    for i in range(len(lis)):
        if(is_float(lis[i])) and '.' in lis[i]:
            num_cost = float(lis[i])
            if(num_cost >max_value):
                max_value = num_cost
            
                

    return max_value


def item_names_quant(lis):## call the second list list[1]
    items = []
    quantity = []
    spec_it = " "
    tmp = 0
   
    count = 1

    for i in range(len(lis)):

        item_phrase = ""

        if( is_int(lis[i]) ):
            tmp = int(lis[i])

        elif(is_float(lis[i]) ):
            tmp = float(lis[i])

        if( (tmp == 1 )& (count == 1) ):
            quantity.append(lis[i])
            items.append( lis[i-1])#goes back
            count += 1
        elif(tmp == count):
            count += 1
                        #need to iterate back wards for name
            quantity.append(lis[i+1])
            index = i-1
            while( not(lis[index].replace('.', '', 1).isdigit() ) ):
                
                item_phrase = lis[index] + " "+ item_phrase
                index -= 1 
            items.append(item_phrase)
            
                    
    return items,quantity
        
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

def find_dates(lis):
    months=['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    ret = []

   # for i in range(len(lis)):

        # if(is_int(lis[i])):
        #     year_guess = int(lis[i])
        #     if((year_guess > 2000) & (year_guess <2023)):
        #         str =  lis[i-2] + ' '+  lis[i-1] + ' ' + lis[i]
        #         ret.append(str)
   # return ret


    for i in range(len(lis)):
        s = lis[i]
        if s in months:
            str = lis[i-1] + ' '+ s + ' ' + lis[i+1]
            ret.append(str)

    return ret
    


def output_data(fields,values, filename):
    fout = open(filename,'w+')
    fout.write('field,value\n')

    for i in range(len(fields)):
        field = fields[i]
        value = values[i]
        fout.write(field+','+value)
        fout.write('\n')

    fout.close()




def main_call(file):
    path =r'C:\Users\migue\OneDrive\Documents\Python\VisonAPIDemo\advert_invoice.jpg'
    
    
    lis = detect_text(file)
    address = find_address(lis[0])
    dates = find_dates(lis[0])
    names, quantities = item_names_quant(lis[1])
    total = find_total(lis[0])
    inv = find_invoice_num(lis[0])
    

    #print(address,dates,names,total,inv, quantities)
    fields = ['Invoice Date', 'Invoice Due Date', 'Invoice ID', 'Address']
    namefields = ['Item name', 'Quantity'] * len(names)

    for field in namefields:
        fields.append(field)

    fields.append('Total Amount/Balance Due')

    values = [dates[0],dates[1],inv,address]

    for i in range(len(names)):
        values.append(names[i])
        values.append(quantities[i])
    values.append(str(total))

    print(fields,values)
    filenam = +str(inv)+'_invoice_output.csv'
    output_data(fields,values,filenam)
    print(dates,address,inv,names,quantities,total)
