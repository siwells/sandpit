

import java.io.IOException;
import java.math.*;
import java.net.URL;
import java.security.*;
import java.util.Arrays;
import java.util.Date;

import twitter4j.*;
import twitter4j.auth.AccessToken;

class TweetTest
{
    public static void main(String[] args) throws Exception, IOException, TwitterException
    {

        //Your Twitter App's Consumer Key
        String consumerKey = "";
         
        //Your Twitter App's Consumer Secret
        String consumerSecret = "";
         
        //Your Twitter Access Token
        String accessToken = "";
        
        //Your Twitter Access Token Secret
        String accessTokenSecret = "";
        
        //Instantiate a re-usable and thread-safe factory
        TwitterFactory twitterFactory = new TwitterFactory();
        
        //Instantiate a new Twitter instance
        Twitter twitter = twitterFactory.getInstance();
        
        //setup OAuth Consumer Credentials
        twitter.setOAuthConsumer(consumerKey, consumerSecret);
        
        //setup OAuth Access Token
        twitter.setOAuthAccessToken(new AccessToken(accessToken, accessTokenSecret));
     
        String now = new Date().toString();
        final MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(now.getBytes("UTF-8"), 0, now.length());

        //Instantiate and initialize a new twitter status update
        StatusUpdate statusUpdate = new StatusUpdate("Testing Tweeting from code: " 
            + new BigInteger(1,md.digest()).toString(16));

        //tweet or update status
        Status status = twitter.updateStatus(statusUpdate);

       //response from twitter server
       System.out.println("status.toString() = " + status.toString());
    }
}
