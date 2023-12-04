// 카카오 로그인 실행 시 새로운 창에서 로그인을 실행할 수 있도록 함수를 만들어 봅니다.
    function socialLoginWindow(loginUrl, redirectUrl) {
        let mainWindow = window;
        let loginWindow = window.open(loginUrl, '_blank', 'width=500, height=600');
        // 로그인이 완료되면 해당 시점에 로그인 창을 닫고 기존의 창으로 돌아가야 합니다.
        // 주기적으로 확인하는 함수
        let checkLoginStatus = setInterval(function() {
            // 로그인이 완료되면 해당 시점에 로그인 창을 닫고 기존의 창으로 돌아가기
            if (loginWindow.location.href === redirectUrl) {
                loginWindow.close();
                clearInterval(checkLoginStatus); // 로그인 확인이 되면 clearInterval로 중지
                mainWindow.location.href = redirectUrl;
            }
        }, 100); // 1초마다 확인 (원하는 주기로 조절)
    }