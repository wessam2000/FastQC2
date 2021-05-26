import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'Login.dart';
import 'Sign_Up.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
      title: 'FASTAQC^2',
      theme: ThemeData(
        primarySwatch:Colors.blue,
    ),
      home:MyHomePage(title: 'FASTAQC^2'),
    );
  }
}
class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);



  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
        title: Text("FASTAQC^2"),
    backgroundColor: Colors.blueGrey,
    leading: Image(image: AssetImage('assets/images/FastaqC^2 Logo.png')),
        ),
        body:Container(
          padding: EdgeInsets.all(10),
          child: ListView(
              children: <Widget>[
                Container(
                  height: 250,
                  padding: EdgeInsets.all(10),
                ),
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(50, 0, 50, 0),
                    child: RaisedButton(

                      textColor: Colors.white,
                      color: Colors.blueGrey,
                      child: Text('Login',),
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context)=>LoginPage()));
                      },
                    )),
                Container(
                    child: Row(
                      children: <Widget>[
                        Text('Does not have account?'),
                        FlatButton(
                          textColor: Colors.blueGrey,
                          child: Text(
                            'Sign Up',
                            style: TextStyle(fontSize: 20),
                          ),
                          onPressed: () {
                            //signup screen
                            Navigator.push(context, MaterialPageRoute(builder: (context)=>SignUpPage()));
                          },
                        )
                      ],
                      mainAxisAlignment: MainAxisAlignment.center,
                    ))

              ]),

        )
    );


  }
}