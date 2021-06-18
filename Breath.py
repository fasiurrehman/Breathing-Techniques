import streamlit  as st
import time
import numpy as np
import altair as alt

options=st.sidebar.slider("Select # of cycles",1,10)
"Time required for ",options," cycles ","is ",int((options*18)/60), " Minutes and",(options*18)%60, "Sconds"


def gettingStarted():
   
    for i in range(0,5):
        st.write(abs(i-5))
        time.sleep(1)


def getBar(time_sec,progress_devide,latest_iteration,text,bar):
    time_per_iteration=(time_sec/progress_devide)-(0.0105)
    
    for i in range(0,progress_devide):
        time.sleep(time_per_iteration)
        latest_iteration.text(f'{text}{int((i/(progress_devide-1))*100)}')
        bar.progress(int((i/(progress_devide-1))*100))
    # bar = st.progress(0)


progress_devide=20
latest_iteration = st.empty()
bar = st.progress(0)



if st.button('Start'):
    "Starting in 5 Seconds Get Ready"
    gettingStarted()
    for iters in range(0,options):
        getBar(4,progress_devide,latest_iteration,"Inhale ",bar)
        getBar(7,progress_devide,latest_iteration,"Hold ",bar)
        getBar(8,progress_devide,latest_iteration,"Exhale ",bar)
    st.write("Done!!")
    st.balloons()
