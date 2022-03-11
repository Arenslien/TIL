# Welcome & Login Screen UI

## 새롭게 배운 점

- Code Refactoring

  - 반복해서 사용되는 위젯들은 새로운 위젯 클래스로 뽑아낸 뒤 여러 속성 값들을
  파라미터로 넘길 수 있게 만듦 -> 코드 가독성 & 재사용성 UP

- Widget

  - ThemeData() : textTheme 속성의 TextTheme 클래스가 사용된다. 이때 옛 문법과 현 문법이 다르기 때문에 함께 사용할 경우 에러가 남. 옛 문법의 textTheme 속성들을 사용할 경우 TextTheme 클래스 내에서 새로 초기화 하지 않고 사용하는 부분에서 불러온 뒤 copyWith() method를 통해 사용해야 함.
  예) style: Theme.of(context).textTheme.button!.copyWith(color: Colors.white),
  - SvgPicture() : 주로 SvgPicture.asset(경로)을 통해 svg 이미지 파일을 사용함
  - Align() : 위젯의 위치를 정렬함. alignment 속성에 Alignment.left 등을 할당하여 사용
  - SingleChildScrollView() : 위젯을 배열해 놓지만 화면 밖을 넘어가는 경우 해당 위젯을 사용하여 해결 가능. 스크롤 기능 추가.
  - Container() & BoxDecoration() : Container 위젯의 decoration 속성에 BoxDecoration 인스턴스를 넘겨주어 활용 가능, 세트로 사용하기에 좋은 조합 -> 이를 기반으로 커스텀 위젯을 만들기 좋음
  - Stack() & Positioned() : 여러 위젯을 겹쳐 사용하여 배치할 때 사용되는 위젯, Stack()을 통해 사용할 위젯들을 순서대로 나열한 후 Positioned()으로 세부 위치 조정
  - FittedBox() : child 위젯에 딱 맞게 사이즈를 조절해주는 위젯

- 느낀점

  - 코드 리팩토링을 할 수 있는 부분은 하는 게 무조건 좋음.
  - Container() & BoxDecoration() 세트는 여러 부분에서 활용 가능.
  - 후에는 상수를 선언할 때 기본적인 padding 값도 설정하는 게 좋을 것 같음.

