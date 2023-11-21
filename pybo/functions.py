# 리다이렉트 url을 반환하는 함수
def get_redirect_url():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    redirect_url = os.environ.get('REDIRECT_URL')

    return redirect_url
