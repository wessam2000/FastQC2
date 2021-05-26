import 'package:flutter/material.dart';
class PerBaseSequanceQuality extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("FASTAQC^2"),
          backgroundColor: Colors.blueGrey,
          leading: Image(image: AssetImage('assets/images/FastaqC^2 Logo.png')),
        ),
          body: Center(
          child: Image(image: AssetImage('assets/images/Quality Scores across all bases.jpg')),
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
