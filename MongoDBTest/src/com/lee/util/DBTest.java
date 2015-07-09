package com.lee.util;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.junit.Before;
import org.junit.Test;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.Mongo;
import com.mongodb.WriteConcern;

public class DBTest {
	private Mongo m;
	private DB db;
	private static String dbName = "lee";

	/*
	 * ��ȡmongo����
	 */
	@Before
	public void getMongo() {
		m = ConnectMongoDB.getDbConnection();
		System.out.println("ConnectMongoDB.getDbConnection :" + m);
		for (String s : m.getDatabaseNames()) {
			System.out.println(s);
		}
	}

	/**
	 * ��ȡ���ݿ���󣬿���չʾ��ӵ�ж��ٸ�����
	 */
	@Before
	public void getDb() {
		db = ConnectMongoDB.getDB(dbName);
		System.out.println("db :" + db);
		for (String s : db.getCollectionNames()) {
			System.out.println(s);
		}
		// DBCollection c = db.getCollection("u");
		// c.drop();
	}

	/**
	 * չʾ��ȡ��mongo ��db ���е�ǰ�ļ���
	 */
	@Test
	public void getCons() {
		Set<String> names = db.getCollectionNames();
		for (String name : names) {
			System.out.println("CollectionName: " + name);
			DBCollection coll = db.getCollection(name);
			System.out.println("CollectionCount=" + coll.count());
			DBCursor cursor = coll.find();
			while (cursor.hasNext()) {
				System.out.println("DBObject=" + cursor.next());
			}
			List<DBObject> objs = coll.getIndexInfo();
			for (DBObject obj : objs) {
				System.out.println("IndexInfo=" + obj);
			}
			System.out.println("----------------------------------");
		}
	}

	/**
	 * ��ѯ��ǰ�����е�������Ϣ
	 */
	@Test
	public void testFind() {
		DBCollection coll = db.getCollection(dbName);
		DBCursor cursor = coll.find();
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			System.out.println(obj);
		}
	}

	/**
	 * ���� 1 ʹ��DBObject���м򵥲���
	 */

	@Test
	public void insert1() {
		DBCollection collection = db.getCollection(dbName);
		DBObject obj = new BasicDBObject();
		obj.put("name", "liwenxin");
		obj.put("age", 25);
		obj.put("address", "xinjiang");
		collection.insert(obj);
	}

	/**
	 * ʹ��DBObject ������Ƕ�ĵ��Ĳ��룬������DBobject��������һ��DBObject
	 */
	@Test
	public void insert2() {
		DBCollection collection = db.getCollection(dbName);
		DBObject obj = new BasicDBObject();
		obj.put("name", "liuxufei");
		obj.put("age", 26);
		obj.put("address", "qinghai");
		DBObject obj2 = new BasicDBObject();
		obj2.put("shengao", "178cm");
		obj2.put("tizhon", "60kg");
		obj.put("xinzi", obj2);
		collection.insert(obj);
	}

	/**
	 * ʹ��map�������в��룬Ҳ���Խ�����Ƕ�ĵ�����
	 */
	@Test
	public void insert3() {
		DBCollection collection = db.getCollection(dbName);
		DBObject obj = new BasicDBObject();
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("name", "lalala");
		map.put("age", 24);
		map.put("address", "shanghai");
		Map<String, Object> map2 = new HashMap<String, Object>();
		map2.put("fuqin", "lala");
		map2.put("muqin", "lala");
		map.put("family", map2);
		obj.putAll(map);
		collection.insert(obj);

	}

	@Test
	public void testFind1() {
		DBCollection coll = db.getCollection(dbName);
		DBCursor cursor = coll.find();
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			System.out.println(obj);
		}
	}

	/**
	 * ɾ������ ɾ�������Ĳ���Ҳ��DBObject
	 */
	@Test
	public void testRemove() {
		DBCollection coll = db.getCollection(dbName);
		DBObject obj = new BasicDBObject();
		obj.put("name", "liwenqiang");
		System.out.println(coll.remove(obj));
	}

	/**
	 * ���²��� ���Ȼ�ȡ����Ȼ���ڽ��в��룬��������Ҫע����ǲ��� $inc ....
	 */
	@Test
	public void update() {
		DBCollection coll = db.getCollection(dbName);
		DBObject obj = new BasicDBObject();
		obj.put("name", "liwenxin");
		DBObject obj2 = new BasicDBObject();
		obj2.put("sallary", 10000);
		DBObject obj3 = new BasicDBObject();
		obj3.put("$inc", obj2);
		System.out.println(coll.update(obj, obj3));
	}

	/**
	 * ������ѯ���򵥵�������ѯ
	 */
	@Test
	public void testFind2() {
		DBCollection coll = db.getCollection(dbName);
		DBObject sera = new BasicDBObject();
		DBObject basi = new BasicDBObject();
		sera.put("$gte", 25);
		basi.put("age", sera);
		DBObject re = new BasicDBObject();
		re.put("name", 1);
		DBCursor cursor = coll.find(basi,re);

		// WriteConcern
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			System.out.println(obj);
		}
	}

	/**
	 * ��ȡ���е�����
	 */
	@Test
	public void getCount() {
		DBCollection collection = db.getCollection(dbName);
		long count = collection.getCount();
		System.out.println(count);

	}

	/**
	 * �оٳ���ѯ�ļ�¼������ û�еĻ���null
	 */
	@Test
	public void testFind4() {
		DBCollection coll = db.getCollection(dbName);
		DBCursor cursor = coll.find();
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			System.out.println(obj.get("name"));
		}
	}

	/**
	 * ��ѯ��Ƕ�ĵ� 1 ���Ҫ��ѯfamily ��muqin�ģ����뽫family����Ϣ������Ľ��� �����޽�� 2
	 * ����ʹ�÷���family.muqin�����滻
	 */
	@Test
	public void find6() {
		DBCollection c = db.getCollection(dbName);
		DBObject boj1 = new BasicDBObject();
		DBObject boj2 = new BasicDBObject();
		// boj1.put("muqin", "lala");
		boj2.put("family.muqin", "lala");
		DBCursor cc = c.find(boj2);
		while (cc.hasNext()) {
			System.out.println(cc.next());
		}

	}

	@Test
	public void find7() {
		DBCollection c = db.getCollection(dbName);
		DBObject boj1 = new BasicDBObject();
		DBObject boj2 = new BasicDBObject();
		boj1.put("muqin", "lala");
		boj1.put("fuqin", "lala");
		boj2.put("family", boj1);
		DBCursor cc = c.find(boj2);
		while (cc.hasNext()) {
			System.out.println(cc.next());
		}

	}
	
	@Test
	public void find0(){
		DBCollection collection = db.getCollection(dbName);
		DBObject o1 = new BasicDBObject();
		o1.put("muqin", "lala");
		DBObject o2 = new BasicDBObject();
		o2.put("family", o1);
		DBObject o3 = new BasicDBObject();
		o3.put("$elemMatch", o2);
		System.out.println(o3);
	}
	
}
