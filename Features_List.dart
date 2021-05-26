import 'package:fastaqc/perBaseSequanceQuality.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'Duplicate sequances.dart';
import 'Overepresented Sequances.dart';
import 'Overrepresented Kmers.dart';
import 'Per Base GC Content.dart';
import 'Per Base N Content.dart';
import 'Per Base Sequance Content.dart';
import 'Per Sequance GC Content.dart';
import 'Per Sequence Quality Scores.dart';
import 'Sequence Length Distribution.dart';
import 'basic_statistics.dart';

class FeaturesList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
        title: Text("FASTAQC^2"),
    backgroundColor: Colors.blueGrey,
    leading: Image(image: AssetImage('assets/images/FastaqC^2 Logo.png')),
        ),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: ListView(
            children: <Widget>[
        Container(
        alignment: Alignment.center,
            padding: EdgeInsets.all(10),
            child: Text(
              'Features',
              style: TextStyle(
                  color: Colors.black,
                  fontWeight: FontWeight.w500,
                  fontSize: 30),
            )),
          Container(
        height: 40,
        //padding: EdgeInsets.fromLTRB(10, 0, 10, 0),
              child:FlatButton(
              child: Text('Basic Statistics'),
              color:Colors.white70,
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>BasicStatistics()));
              },
            ),
          ),
  Container(
    child:  FlatButton(
      child: Text('PerBase Sequance Quality',textAlign: TextAlign.start,),
      color:Colors.white70,
      onPressed: (){
        Navigator.push(context, MaterialPageRoute(builder: (context)=>PerBaseSequanceQuality()));
      },
    ),
      ),
              Container(
                child:  FlatButton(
                  child: Text('Per Base Sequance Quality Scores',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerSequenceQualityScores()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Per Base Sequance Content',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerBaseSequanceContent()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Per Base GC Content',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerBaseGCContent()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Per Sequance GC Content',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerSequanceGCContent()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Per Base N Content',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>PerBaseNContent()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Sequance Lenghth Discribution',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>SequenceLengthDistribution()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text(' Dublicate Sequances',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>Duplicatesequances()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Overrepresented Sequances',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>OverepresentedSequances()));
                  },
                ),
              ),
              Container(
                child:  FlatButton(
                  child: Text('Overrepresented Kmers',textAlign: TextAlign.start,),
                  color:Colors.white70,
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>OverrepresentedKmers()));
                  },
                ),
              ),
        ],
      ),
    ));
  }
}
