import streamlit as st

with st.form(key='profile_from'):
    #テキストボックス
    name = st.text_input('名前')
    adress = st.text_input('住所')

    #セレクトボックス(st.selectboxをst.radioに変更可能)
    age_category = st.selectbox(
        '年齢層',
        ('子供(18歳未満)','大人(18歳以上)'))
    
    #複数選択
    hobby = st.multiselect(
            '趣味',
            ('スポーツ','ゲーム','読書','プログラミング','釣り','睡眠','料理'))

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{adress}に手紙を送信しました。')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {", ".join(hobby)}')