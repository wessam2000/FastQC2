import 'package:flutter/material.dart';
class PerBaseSequanceQuality extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title:Text("PerBaseSequanceQuality"),
          backgroundColor: Colors.black12,
          leading: Image(image: AssetImage('assets/images/Fastaqc Logo.png')),
        ),
          body: Center(
          child: Image(image: AssetImage('assets/images/Per Base Sequance Quality.jpg')),
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
