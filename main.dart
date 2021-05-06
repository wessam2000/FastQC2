import 'package:fastaqc/perBaseSequanceQuality.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:fastaqc/basic_statistics.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'FastaqC',
      theme: ThemeData(
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'FastaqC'),
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
        title: Text(widget.title),
        backgroundColor: Colors.black12,
        leading: Image(image: AssetImage('assets/images/Fastaqc Logo.png')),
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children:[
           Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children:[
            FlatButton(
            child: Text('BasicStatistics'),
            color:Colors.black12,
            onPressed: (){
              Navigator.push(context, MaterialPageRoute(builder: (context)=>BasicStatistics()));
            },
        ),
          ]),
        Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children:[
                FlatButton(
                  child: Text('PerBaseSequanceQuality'),
                  color:Colors.black12,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerBaseSequanceQuality()));
                  },
                ),
              ]),

       
        ])
    );
  }
  }