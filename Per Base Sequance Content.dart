import 'package:flutter/material.dart';
class PerBaseSequanceContent extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("FASTAQC^2"),
          backgroundColor: Colors.blueGrey,
          leading: Image(image: AssetImage('assets/images/FastaqC^2 Logo.png')),
        ),
        body: Center(
          child: Image(image: AssetImage('assets/images/Per Base Sequance Content.jpg')),
        ),
        bottomNavigationBar:FlatButton(
          child: Icon(Icons.arrow_back_ios,),
          onPressed: (){
            Navigator.pop(context);
          },
        )
    );

  }
}
