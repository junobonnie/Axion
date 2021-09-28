# Axion

![ax_icon_bare](https://user-images.githubusercontent.com/60418809/135108433-867bd7c2-13b4-482d-9efe-8d4dc71d1f24.png)

설명: image hashing based duplicate photo finder

사용한 라이브러리: pyqt 사용

라이센스: GNU GPL LISENCE</br></br></br>

## 원리

![image](https://user-images.githubusercontent.com/60418809/135102062-8a409f2a-3f78-43dc-bcf3-29174ee07a06.png)

이미지를 (16, 16, 16) 크기로 변환한 후 그것을 다시 RSA-256 해쉬로 변환합니다. 이 이미지 해쉬값을 비교하여 중복 검사를 합니다. 유사 이미지 검색을 위해 머신러닝이나 딥러닝 알고리즘을 이용하지 않기 때문에 빠른 속도로 작동할 것으로 기대합니다. 또한 메모리에서 이미지 자체가 아니라 이미지 해쉬값을 저장하기 때문에 메모리를 크게 절약할 수 있습니다. </br></br></br>


## 주요 기능 및 사용법

![use4](https://user-images.githubusercontent.com/60418809/135101807-fa033421-ac2d-40ce-83ab-c70c9ebcf69d.png)

중복되는 이미지를 찾아서 파일 크기 순으로 디스플레이 해주고, 파일명, 파일 최종 수정일, 이미지 크기, 이미지 해상도, 파일 크기 정보를 제공합니다.</br></br></br>


![image](https://user-images.githubusercontent.com/60418809/135103828-47294db3-9ce5-489b-9527-67de05b8b99d.png)

서로 다른 폴더에 있는 이미지끼리도 중복 검사를 할 수 있습니다. 또한 하위 경로 탐색을 통해 하위 경로에 있는 모든 이미지의 중복검사가 가능합니다.</br></br></br>

![log](https://user-images.githubusercontent.com/60418809/135101821-6329345e-e2db-47a9-9f68-f6fe2d68eab1.png)

로그 창을 통해 어떤 파일이 검사가 되지 않았는지, 어떤 파일들이 중복 되었는지 텍스트 정보로 확인할 수 있습니다.</br></br></br>

![config](https://user-images.githubusercontent.com/60418809/135101669-efd8ad14-e674-4c0c-93bf-14c920589230.gif)

설정창을 통해 이미지 중복 검사 설정을 바꿀 수 있습니다.</br></br></br>

![use](https://user-images.githubusercontent.com/60418809/135101734-d4509f6c-f28e-4fce-81d3-25da8eefd74c.gif)

![use2](https://user-images.githubusercontent.com/60418809/135101742-bc8cf69a-a9d3-44f1-a9ab-58bbe75f13b5.gif)

이미지 중복 검사 설정을 더 단순한 단순화 이미지로 바꾸면 더 많은 유사 이미지를 색출할 수 있습니다. 

또한 삭제 체크 박스와 하단의 삭제 버튼을 통해 중복 이미지를 일괄 삭제할 수 있습니다.</br></br></br>

![use3](https://user-images.githubusercontent.com/60418809/135115751-40a00fca-67fc-418e-a4ba-decb5a08e025.gif)

gif 이미지의 경우 마우스 커서를 이미지 위에 올리면 해당 이미지가 재생됩니다.

이미지 2200여장을 중복 검사하는데 25초가 걸리는 것으로 확인하였습니다.</br></br></br>

## 지원되는 이미지 확장자

  중복 검사가 되고 결과창에 디스플레이도 됨: jpg, jpeg, png, gif, 정적 webp, orig

  중복 검사는 되는데 결과창에 디스플레이가 안됨:  동적 webp (webp 움짤), dds

  중복 검사가 안됨: 없음.

  나머지 확장자: 지원 여부를 확인 안함.</br></br></br>
  
## 업데이트 내용

v0.2 변경사항: </br>
탐색 폴더에 파일이 없을때 progressbar에 발생하는 zero division error fix함. </br>
실행 파일 크기를 300MB에서 45.5MB로 줄임. </br>
결과창 디자인 변경. </br>
결과창에서 보여주는 파일 정보에 파일 최종 수정일과 이미지 가로 세로 크기, 이미지 해상도를 추가. </br>
사용 편의성을 위해 프로그램을 껐다 켜도 최근 열었던 폴더의 상위폴더에서 파일 다이알로그가 열리게 함.</br></br></br>


## 다운로드 링크
v0.2(beta) (windows) Download Link: http://a76f41d0e826.ap.ngrok.io/index.php/s/NsRaaMqqRTNNxr6/download/AXION-v0.2.zip

v0.1(beta) (windows) Download Link: https://drive.google.com/file/d/17HOlNr8IW9qmAyH7SaNyaK6-hx_k_AbK/view?usp=sharing
