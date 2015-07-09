package com.lee.util;

import org.apache.log4j.Logger;
import org.bson.BSON;

import java.net.UnknownHostException;
import java.util.Set;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.DBTCPConnector;
import com.mongodb.Mongo;
import com.mongodb.MongoException;

public class ConnectMongoDB {
	/**
	 * Logger for this class
	 */
	private static final Logger logger = Logger.getLogger(ConnectMongoDB.class);
	// private static Mongo mongo ;
	// private static DBTCPConnector dbtcpConnector;
	// private static DB db;
	private static String hostName = "127.0.0.1";
	private static int port = 27017;

	public static Mongo getDbConnection() {
		Mongo m = null;
		try {
			m = new Mongo(hostName, port);
		} catch (UnknownHostException e) {
			logger.debug("UnknownHostException");
			e.printStackTrace();
		} catch (MongoException e) {
			logger.debug("MongoException");
			e.printStackTrace();
		}

		return m;
	}

	// try {
	// m = new Mongo("127.0.0.1",27017);
	// db = m.getDB("lee");
	// DBCollection coll = db.getCollection("lee");
	// DBObject o = new BasicDBObject();
	// o.put("age", 25);
	// DBCursor cursor = coll.find(o);
	// while (cursor.hasNext()) {
	// System.out.println(cursor.next());
	// }
	// } catch (UnknownHostException | MongoException e) {
	// logger.info("连接数据库出现问题");
	// e.printStackTrace();
	// }
	public static void closeConnection(DB db, String dbName) {
		db.collectionExists(dbName);
	}

	public static DB getDB(String dbName) {
		Mongo m = getDbConnection();
		DB db = null;
		db = m.getDB(dbName);
		return db;
	}
}
