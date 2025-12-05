import streamlit as st
import pickle
from PIL import Image

model=pickle.load(open('rfmodel.sav','rb'))
scaler=pickle.load(open('stdscaler.sav','rb'))

def  main():
    st.title(":red[WINE QUALITY PREDICTION]")
    image=Image.open('wine.jpeg')
    st.image(image,width=500)


    fixed_acidity= st.number_input(":red[fixed acidity]")
    volatile_acidity= st.number_input(":red[volatile acidity]")
    citric_acid= st.number_input(":red[citric acid]")
    residual_sugar= st.number_input(":red[residual sugar]")
    chlorides= st.number_input(":red[chlorides]")
    free_sulfur_dioxide= st.number_input(":red[free sulfur dioxide]")
    total_sulfur_dioxide= st.number_input(":red[total sulfur dioxide]")
    density= st.number_input(":red[density]")
    pH= st.number_input(":red[pH]")
    sulphates= st.number_input(":red[sulphates]")
    alcohol=st.number_input(":red[alcohol]")
    


    features = [[
    float(fixed_acidity), float(volatile_acidity), float(citric_acid),
    float(residual_sugar), float(chlorides), float(free_sulfur_dioxide),
    float(total_sulfur_dioxide), float(density), float(pH),
    float(sulphates), float(alcohol)
]]


    

    pred=st.button('PREDICT')

    if pred:
        feature=scaler.transform(features)
        prediction=model.predict(feature)
        pred_value = float(prediction[0])

        if pred_value in [1, 2, 3, 4]:
            st.write("BAD QUALITY WINE")
        elif pred_value in [5, 6]:
            st.write("AVERAGE QUALITY WINE")
        elif pred_value in [7, 8, 9, 10]:
            st.write("GOOD QUALITY WINE")

main()
