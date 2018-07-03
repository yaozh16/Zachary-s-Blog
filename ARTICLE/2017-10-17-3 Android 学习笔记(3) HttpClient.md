# 2017-10-17-3 Android 学习笔记(3) HttpClient

## 1、Get
###  不带参数的Get请求
```java
HttpClient httpClient = new DefaultHttpClient();
HttpGet httpGet = new HttpGet("http://www.w3cschool.cc/python/python-tutorial.html");
HttpResponse httpResponse = httpClient.execute(httpGet);
if (httpResponse.getStatusLine().getStatusCode() == 200) {
    HttpEntity entity = httpResponse.getEntity();
    detail = EntityUtils.toString(entity, "utf-8");
}
```

### 带有参数的Get请求
```java
List<BasicNameValuePair> params = new LinkedList<BasicNameValuePair>();  
params.add(new BasicNameValuePair("user", "猪小弟"));  
params.add(new BasicNameValuePair("pawd", "123"));
String param = URLEncodedUtils.format(params, "UTF-8"); 
HttpGet httpGet = new HttpGet("http://www.baidu.com"+"?"+param);
```

## 2、Post
Post 方法传入参数时，需要先导入到List<NameValuePair>中，然后通过httpPost.setEntity方法设置进去
```java
HttpClient httpClient = new DefaultHttpClient();
HttpPost httpPost = new HttpPost(url);
List<NameValuePair> params = new ArrayList<NameValuePair>();
params.add(new BasicNameValuePair("user", "猪大哥"));
params.add(new BasicNameValuePair("pawd", "123"));
UrlEncodedFormEntity entity = new UrlEncodedFormEntity(params,"UTF-8");
httpPost.setEntity(entity);
HttpResponse httpResponse =  httpClient.execute(httpPost);//执行Post,实际上Get也可以通过这种方法实现
if (httpResponse.getStatusLine().getStatusCode() == 200) {
    HttpEntity entity2 = httpResponse.getEntity();
    //EntityUtils是类名
    detail = EntityUtils.toString(entity2, "utf-8");
}
```

## 3、其他

* 获取cookie
```java
// 获取响应的cookie值
cookie = httpResponse.getFirstHeader("Set-Cookie").getValue();
```
* 发送Post请求,禁止重定向
```java
HttpPost httpPost = new HttpPost(true_url);
httpPost.getParams().setParameter(ClientPNames.HANDLE_REDIRECTS, false);
```
* 设置Post提交的头信息的参数
```java
httpPost.setHeader("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko");
httpPost.setHeader("Referer", true_url);
httpPost.setHeader("Cookie", cookie);
```
* 设置编码方式,响应请求,获取响应状态码:
```java
httpPost.setEntity(new UrlEncodedFormEntity(params, "gb2312"));
HttpResponse response = new DefaultHttpClient().execute(httpPost);
```

## 4、使用HttpPut发送Put请求
```java
HttpPut httpPut = new HttpPut(PUTACKCODE_URL);
httpPut.setHeader("Cookie", cookie);
try {
  List<NameValuePair> params = new ArrayList<NameValuePair>();
  params.add(new BasicNameValuePair("activation_code", actCode));
  params.add(new BasicNameValuePair("license_plate", licPlate));
  httpPut.setEntity(new UrlEncodedFormEntity(params, "UTF-8"));
  HttpResponse course_response = new DefaultHttpClient().execute(httpPut);
  if (course_response.getStatusLine().getStatusCode() == 200) {
      HttpEntity entity2 = course_response.getEntity();
      JSONObject jObject = new JSONObject(EntityUtils.toString(entity2));
      resp = Integer.parseInt(jObject.getString("status_code"));
      return resp;
  }
} catch (Exception e) {
  e.printStackTrace();
}
```
