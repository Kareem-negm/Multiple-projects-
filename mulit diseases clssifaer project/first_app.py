import pandas as pd
import webbrowser
import streamlit as st
import pickle
from PIL import Image

#______________________________________________________________________


st.header("""
Get the probability of you having a disease of the following diseases. Select the disease to start the test
""")

st.write('')
st.write('')


st.write('\n For the questionnaires that ask about body temperature/current Heart pulse rate,  use the measuring tool to enter the accurate values.')
st.write(' \n You are free to check your body condition whenever you want regardless of the web app.')

st.write('')
st.write('')

image = Image.open('C:/Users/negmk/Desktop/mulit diseases for stem/photo.png')
st.image(image ,hight =700 ,width=700 )







#__________________________________________________________________

#loade the models 

cancer_model = pickle.load(open("C:/Users/negmk/Desktop/mulit diseases for stem/models/breast_cancer.pkl", 'rb'))
diabe_model= pickle.load(open("C:/Users/negmk/Desktop/mulit diseases for stem/models/diabetes.pkl", 'rb'))
heart_model= pickle.load(open("C:/Users/negmk/Desktop/mulit diseases for stem/models/heart.pkl", 'rb'))
kind_model= pickle.load(open("C:/Users/negmk/Desktop/mulit diseases for stem/models/kidney2.pkl", 'rb'))
liver_model= pickle.load(open("C:/Users/negmk/Desktop/mulit diseases for stem/models/liver.pkl", 'rb'))

#_______________________________________________________________________



#st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)


st.write('Please chose what kind of disease you want to predicate')
cancer_button = st.button(label='cancer')
diabe_button = st.button(label='diaberes')
heart_button = st.button(label='heart')
kind_button = st.button(label='kidney')
liver_button = st.button(label='liver')
conniction = st.sidebar.button(label='conect us ')

#_______________________________________________________________________

#Breast Cancer Predictor
if cancer_button:

    #Get the feature input from the user
    def get_user_input1():
        radius_mean = st.number_input('radius_mean')
        texture_mean = st.number_input("texture_mean")
        perimeter_mean = st.number_input('perimeter_mean')
        area_mean = st.number_input(' area_mean')
        smoothness_mean= st.number_input('smoothness_mean')
        compactness_mean = st.number_input("compactness_mean")
        concavity_mean = st.number_input('concavity_mean')
        concave_points_mean = st.number_input('concave_points_mean')
        symmetry_mean = st.number_input('symmetry_mean')
        radius_se  = st.number_input('radius_se')
        perimeter_se  = st.number_input('perimeter_se')
        area_se  = st.number_input('area_se')
        compactness_se = st.number_input('compactness_se')
        concavity_se = st.number_input('concavity_se')
        concave_points_se  = st.number_input("concave_points_se")
        fractal_dimension_se  = st.number_input('fractal_dimension_se')
        radius_worst = st.number_input('radius_worst')
        texture_worst  = st.number_input('texture_worst')
        perimeter_worst = st.number_input('perimeter_worst')
        area_worst = st.number_input('area_worst')
        smoothness_worst  = st.number_input('smoothness_worst')
        compactness_worst  = st.number_input('compactness_worst')
        concavity_worst  = st.number_input('concavity_worst')
        concave_points_worst = st.number_input('concave_points_worst')
        symmetry_worst = st.number_input('symmetry_worst')
        fractal_dimension_worst  = st.number_input("fractal_dimension_worst")
 
   
        user_data1 = {'radius_mean ': radius_mean ,
              'texture_mean ': texture_mean ,
                 'perimeter_mean ': perimeter_mean ,
                 'area_mean ': area_mean ,
              'rsmoothness_meanbc ': smoothness_mean ,
              'compactness_mean ': compactness_mean ,
                 'concavity_mean ': concavity_mean ,
                 'concave_points_mean  ': concave_points_mean  ,
                 'symmetry_mean  ': symmetry_mean  ,
                 'radius_se  ': radius_se  ,
                 'perimeter_se  ': perimeter_se ,
                 'area_se ': area_se ,
                 'compactness_se  ': compactness_se  ,
                 'concavity_se  ': concavity_se  ,
                 'concave_points_se  ': concave_points_se  ,
                 'fractal_dimension_se  ': fractal_dimension_se  ,
                 'radius_worst  ': radius_worst  ,
                 'texture_worst  ': texture_worst  ,
                 'perimeter_worst  ': perimeter_worst  ,
                 'area_worst  ': area_worst  ,
                 'smoothness_worst  ': smoothness_worst  ,
                 'compactness_worst  ': compactness_worst  ,
                 'concavity_worst  ': concavity_worst  ,
                 'concave_points_worst  ': concave_points_worst  ,
                 'symmetry_worst  ': symmetry_worst  ,
                 'fractal_dimension_worst  ': fractal_dimension_worst  ,
                 
                 }

        features1 = pd.DataFrame(user_data1, index=[0])
        return features1

    user_input1 = get_user_input1()

    st.subheader('User Input :')
    st.write(user_input1)
      
    predict_button1 = st.button(label='Predict')

    if predict_button1:

        prediction = cancer_model.predict(user_input1)
        
        st.subheader('Classification: ')
        st.write(prediction)
    
        st.subheader('predicted probabilities: ')

        prediction_proba = cancer_model.predict_proba(user_input1)
        st.write(prediction_proba)

        if prediction==0:
    
            st.subheader('you dont have Cancer disease , Enjoy and preserve your life')
        else:
            st.subheader('you have Cancer disease , please Click on the next button to go to the tips page and go to the doctor as soon as possible')  
            
            url = 'https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/managing'

            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

#_________________________________________________________________________________________________________________________

#Breast diabe Predictor
if diabe_model:
    
    #Get the feature input from the user
    def get_user_input2():

        pregnancies = st.number_input('pregnancies')
        glucose = st.number_input("glucose")
        bloodpressure = st.number_input('bloodpressure')
        skinthickness = st.number_input(' skinthickness')
        insulin= st.number_input('insulin')
        bmi = st.number_input("bmi")
        dpf = st.number_input('dpf')
        age = st.number_input('age')


        user_data2= {'pregnancies ': pregnancies ,
              'glucose ': glucose ,
                 'bloodpressure ': bloodpressure ,
                 'skinthickness ': skinthickness ,
              'insulin ': insulin ,
              'bmi ': bmi ,
                 'dpf ': dpf ,
                 'age  ': age 
                 
                 }


        features2 = pd.DataFrame(user_data2, index=[0])

        return features2


    user_input2 = get_user_input2()

    st.subheader('User Input :')
    st.write(user_input2)
      
    predict_button2 = st.button(label='Predict2')

    if predict_button2:

        prediction = cancer_model.predict(user_input2)
        st.subheader('Classification: ')
        st.write(prediction)
    
        st.subheader('predicted probabilities: ')

        prediction_proba = cancer_model.predict_proba(user_input2)
        st.write(prediction_proba)

        if prediction==0:
    
            st.subheader('you dont have Cancer disease , Enjoy and preserve your life')
        else:
            st.subheader('you have Cancer disease , please Click on the next button to go to the tips page and go to the doctor as soon as possible')  

            url = 'https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/managing'

            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

#____________________________________________________________________________________________________________________________


#Breast heart Predictor
if heart_model:

    #Get the feature input from the user
    def get_user_input3():

        age = st.number_input('age3')
        sex = st.number_input("sex(Male:1, female:0)")
        cp = st.number_input('chest pain type')
        trestbps = st.number_input(' resting blood pressure in mm Hg')
        chol = st.number_input(' serum cholestoral in mg/dl')
        fbs= st.number_input('fasting blood sugar 120 mg/dl(1 = true; 0 = false)')
        restecg = st.number_input("resting electrocardiographic results")
        thalach = st.number_input('maximum heart rate achieved')
        exang = st.number_input('exercise induced angina (1 = yes; 0 = no)')
        oldpeak = st.number_input('ST depression induced by exercise relative to res')
        slope  = st.number_input('the slope of the peak exercise ST segment')
        ca  = st.number_input('number of major vessels (0-3) colored by flourosopy')
        thal  = st.number_input('3 = normal; 6 = fixed defect; 7 = reversable defect')
   
        user_data3 = {'age ': age ,
              'sex ': sex ,
                 'cp ': cp ,
                 'trestbps ': trestbps ,
                 'chol ': chol ,
              'fbs ': fbs ,
              'restecg ': restecg ,
                 'thalach ': thalach ,
                 'exang  ': exang  ,
                 'oldpeak  ': oldpeak  ,
                 'slope  ': slope  ,
                 'ca  ': ca ,
                 'thal ': thal 
                 }


        features3 = pd.DataFrame(user_data3, index=[0])

        return features3

    user_input3 = get_user_input3()

    st.subheader('User Input :')
    st.write(user_input3)
      

    predict_button3 = st.button(label='Predict3')

    if predict_button3:

        prediction = cancer_model.predict(user_input3)

        st.subheader('Classification: ')
        st.write(prediction)
    
        st.subheader('predicted probabilities: ')
        prediction_proba = cancer_model.predict_proba(user_input3)
        st.write(prediction_proba)

        if prediction==0:
    
            st.subheader('you dont have Cancer disease , Enjoy and preserve your life')
        else:
            st.subheader('you have Cancer disease , please Click on the next button to go to the tips page and go to the doctor as soon as possible')   
            
            url = 'https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/managing'

            if st.button('Open browser'):
                webbrowser.open_new_tab(url)


#_________________________________________________________________________________________________________________________


#Breast kind Predictor
if kind_model:

    #Get the feature input from the user
    def get_user_input4():
        
        age = st.number_input('age4')
        bp = st.number_input("bp")
        al = st.number_input('al')
        su = st.number_input(' su')
        rbc= st.number_input('rbc')
        pc = st.number_input("pc")
        pcc = st.number_input('pcc')
        ba = st.number_input('ba')
        bgr = st.number_input('bgr')
        bu  = st.number_input('bu')
        sc  = st.number_input('sc')
        pot  = st.number_input('pot')
        wc = st.number_input('wc')
        htn = st.number_input('htn')
        dm  = st.number_input("dm")
        cad  = st.number_input('cad')
        pe = st.number_input('pe')
        ane  = st.number_input('ane')



   
        user_data4 = {'age ': age ,
              'bp ': bp ,
                 'al ': al ,
                 'su ': su ,
              'rbc ': rbc ,
              'pc ': pc ,
                 'pcc ': pcc ,
                 'ba  ': ba  ,
                 'bgr  ': bgr  ,
                 'bu  ': bu  ,
                 'sc  ': sc ,
                 'pot ': pot ,
                 'wc  ': wc  ,
                 'htn  ': htn  ,
                 'dm  ': dm  ,
                 'cad  ': cad  ,
                 'pe  ': pe  ,
                 'ane  ': ane 
                 }


        features4 = pd.DataFrame(user_data4, index=[0])
        return features4

    user_input4 = get_user_input4()

    st.subheader('User Input :')

    st.write(user_input4)
      
    predict_button4 = st.button(label='Predict4')

    if predict_button4:


        prediction = cancer_model.predict(user_input4)

        st.subheader('Classification: ')
        st.write(prediction)
    
        st.subheader('predicted probabilities: ')

        prediction_proba = cancer_model.predict_proba(user_input4)
        st.write(prediction_proba)

        if prediction==0:
    
            st.subheader('you dont have Cancer disease , Enjoy and preserve your life')
       
        else:

            st.subheader('you have Cancer disease , please Click on the next button to go to the tips page and go to the doctor as soon as possible')  

            url = 'https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/managing'

            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

#_________________________________________________________________________________________________________________________

#Breast liver Predictor
if liver_model:

    #Get the feature input from the user
    def get_user_input5():
        Age = st.number_input('Age5')
        Total_Bilirubin = st.number_input("Total_Bilirubin")
        Direct_Bilirubin = st.number_input('Direct_Bilirubin')
        Alkaline_Phosphotase = st.number_input(' Alkaline_Phosphotase')
        Alamine_Aminotransferase= st.number_input('Alamine_Aminotransferase')
        Aspartate_Aminotransferase = st.number_input("Aspartate_Aminotransferase")
        Total_Protiens = st.number_input('Total_Protiens')
        Albumin = st.number_input('Albumin')
        Albumin_and_Globulin_Ratio = st.number_input('Albumin_and_Globulin_Ratio')
        Gender_Male  = st.number_input('Gender_Male')
 
   
        user_data5 = {
            'Age ': Age ,
              'Total_Bilirubin ': Total_Bilirubin ,
                 'Direct_Bilirubin ': Direct_Bilirubin ,
                 'Alkaline_Phosphotase ': Alkaline_Phosphotase ,
              'Alamine_Aminotransferase ': Alamine_Aminotransferase ,
              'Aspartate_Aminotransferase ': Aspartate_Aminotransferase ,
                 'Total_Protiens ': Total_Protiens ,
                 'Albumin  ': Albumin  ,
                 'Albumin_and_Globulin_Ratio  ': Albumin_and_Globulin_Ratio  ,
                 'Gender_Male  ': Gender_Male  ,

                 
                 }

        features5 = pd.DataFrame(user_data5, index=[0])

        return features5

    user_input5 = get_user_input5()

    st.subheader('User Input :')
    st.write(user_input5)

      
    predict_button5 = st.button(label='Predict5')

    if predict_button5:

        prediction = cancer_model.predict(user_input5)
        st.subheader('Classification: ')
        st.write(prediction)
    
        st.subheader('predicted probabilities: ')
        
        prediction_proba = cancer_model.predict_proba(user_input5)
        st.write(prediction_proba)

        if prediction==0:
    
            st.subheader('you dont have Cancer disease , Enjoy and preserve your life')
        else:
            st.subheader('you have Cancer disease , please Click on the next button to go to the tips page and go to the doctor as soon as possible') 
               
            url = 'https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/managing'

            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

#_________________________________________________________________________________________________________________________

if conniction:
    st.sidebar.write('Aya Osama')

    st.sidebar.write(' aya.2118109@stemkalubya.moe.edu.eg')
    
    st.sidebar.write('Sarah Gamal')

    st.sidebar.write('sarah.2118163@stemkalubya.moe.edu.eg')
    
    st.sidebar.write('Hagar Ali')

    st.sidebar.write('hagar.211852@stemkalubya.moe.edu.eg')










