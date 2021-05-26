import"package:flutter/material.dart";

import 'Features_List.dart';
class UploadPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        appBar: AppBar(
        title: Text("FASTAQC^2"),
    backgroundColor: Colors.blueGrey,
    leading: Image(image: AssetImage('assets/images/FastaqC^2 Logo.png')),
    ),
        body: Container(
          padding: EdgeInsets.all(10),
            child: ListView(
                children: <Widget>[
                  Container(
                      height: 250,
                      padding: EdgeInsets.all(10),
                      ),
                  Container(
                      alignment: Alignment.center,
                      padding: EdgeInsets.all(10),
                      child: Text(
                        'UploadFile',
                        style: TextStyle(
                            color: Colors.black,
                            fontWeight: FontWeight.w500,
                            fontSize: 30),
                      )),
                  Container(
                    padding: EdgeInsets.all(10),
                    child: TextField(
                     // controller: nameController,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(),
                        labelText: 'Choose File',
                      ),
                    ),
                  ),
                  Container(
                      height: 50,
                      padding: EdgeInsets.fromLTRB(10, 0, 10, 0),
                      child: RaisedButton(
                        textColor: Colors.white,
                        color: Colors.blueGrey,
                        child: Text('UPLOAD'),
                        onPressed: () {
                          Navigator.push(context, MaterialPageRoute(builder: (context)=>FeaturesList()));
                          //print(nameController.text);
                          //print(passwordController.text);
                        },
                      )
                  ),
    ]
            )
        )
    );
  }
}
