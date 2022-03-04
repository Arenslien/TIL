# Welcome & Login Screen UI -> 

## 새롭게 배운 점

- 프로젝트 기본 구조에 필요한 요소

  - project/constants.dart : 전반적인 프로젝트에서 사용될 상수 선언
  - project/assets/.. : 프로젝트에서 사용될 이미지 파일 저장

- Widget

  - ThemeData() : 프로젝트에서 사용되는 여러 UI적인 테마들을 공통적으로 관리하는 위젯
  - Expanded() : child 위젯의 크기를 확장하는 위젯, flex 속성을 통해 비율 설정 가능
  - Container() & BoxDecoration() : Container 위젯의 decoration 속성에 BoxDecoration 인스턴스를 넘겨주어 활용 가능, 세트로 사용하기에 좋은 조합 -> 이를 기반으로 커스텀 위젯을 만들기 좋음
  - RichText() & TextSpan() : 다양한 스타일의 텍스트를 사용할 때 활용 가능한 RichText, TextSpan 트리로 구성된다. 다양한 스타일의 구성은 TextSpan에서 세부적으로 설정
  - FittedBox() : child 위젯에 딱 맞게 사이즈를 조절해주는 위젯
  - Spacer() : 위젯과 위젯 사이에 빈 공간으로 꽉 채우게 하는 위젯.
  - TextField() & InputDecoration() : 기본적인 Text입력 위젯, decoration 속성을 통해 다양한 InputDecoration 활용 가능

- 느낀점

  - 실제로 사용되는 어플의 UI를 비슷하게 구현하는 방법이 실력 향상에 도움이 될 것 같다.
  - 클론코딩하며 새로 알게된 위젯들을 사용해보는 복습이 필요할 것 같다.