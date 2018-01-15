#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

class Node:
	def __init__(self, nodeid):
		self.nodeid = nodeid;
		self.subs = [] ;

	def addSub(self, nodestr):
		self.subs.append( Node(nodestr) );


class Operator(Node):
	def addSub(self, nodestr):
		self.input = "";
		self.outputs = "";

		self.subs.append( Operator(nodestr) );
		#print("subs-", self.subs)

	def execute(self, params):
		print('Operator Execute...', self.nodeid )
		for x in self.subs:
			x.execute(params);


class CsvFileOperator(Operator):

	def setInput(self, inputs):
		self.inputs = inputs;

	def setOutput(self, outputs):
		self.outputurl = outputs;

	def execute(self, params):
		print('CsvFileOperator Execute...', self.nodeid )
		inputData = np.loadtxt( self.inputs, dtype=np.str, delimiter=",");
		
		outputData = inputData ;

		np.savetxt( self.outputurl , outputData , fmt="%s", delimiter = ',');
		for x in self.subs:
			x.execute(params);


class Flow:
	def __init__(self, flowid):
		self.flowid = flowid;
		self.root = None; 

	def setRoot(self, node):
		self.root = node;	

	def run(self, params):
		self.root.execute(params);

		for x in self.root.subs:
			#print("type,",type(x))
			x.execute(params);


#Test code 
def test():
	f = Flow("flow101");
	f.root = Node("n0");
	f.root.addSub( "n1");
	f.root.addSub( "n2");
	f.root.addSub( "n3");

	f.root.subs[1].addSub("n3-0");
	f.root.subs[1].addSub("n3-1");
	f.root.subs[1].addSub("n3-2");

	for x in f.root.subs:
		print('node:',x.nodeid)
		if(len(x.subs) >0):
			for y in x.subs:
				print('   node',y.nodeid)


def testFlow():
	f = Flow("flow101");
	rootOp = CsvFileOperator("n0");
	rootOp.setInput ( "event.csv" );
	rootOp.setOutput ( "event_output.csv" ) ;
	f.root = rootOp;

	f.root.addSub( "n1");
	f.root.addSub( "n2");
	f.root.addSub( "n3");

	f.root.subs[1].addSub("n3-0");
	f.root.subs[1].addSub("n3-1");
	f.root.subs[1].addSub("n3-2");

	f.root.subs[1].subs[0].addSub("n3-0-1");

	params = { "jobid":"job1", "type":"python", "scheduler":"now"};
	f.run( params );

if __name__ == '__main__':
	#test();	
	testFlow();


