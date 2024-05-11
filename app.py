import streamlit as st
from PIL import Image
from io import BytesIO

# アプリのタイトルを設定
st.title('画像縮小するアプリ')

# 画像アップロード用のウィジェットを作成
uploaded_file = st.file_uploader("画像をアップロードしてください", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # アップロードされた画像を読み込む
    image = Image.open(uploaded_file)

    # アップロードされた画像を表示
    st.image(image, caption='アップロードされた画像', use_column_width=True)

    # 縮小後のサイズをユーザーに入力させる
    st.subheader('縮小後のサイズを指定してください')
    width = st.number_input('幅', min_value=1, value=image.width // 2)  # デフォルト値は元の幅の半分
    height = st.number_input('高さ', min_value=1, value=image.height // 2)  # デフォルト値は元の高さの半分

    # サイズ変更ボタン
    if st.button('画像を縮小'):
        # 画像を指定されたサイズに縮小
        resized_image = image.resize((width, height))

        # 縮小した画像を表示
        st.image(resized_image, caption='縮小後の画像', use_column_width=True)

        # 縮小した画像をダウンロードするためのリンクを生成
        buf = BytesIO()
        resized_image.save(buf, format='PNG')
        byte = buf.getvalue()

        st.download_button(
            label="縮小した画像をダウンロード",
            data=byte,
            file_name="resized_image.png",
            mime="image/png"
        )
