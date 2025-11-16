---
title: "Server-sent event event source API client in ObjC for iOS and Mac using NSURLSession"
date: 2013-10-12T00:00:00Z
tags: ["ios"]
---
[TRVSEventSource](https://github.com/travisjeffery/TRVSEventSource) provides an api for opening an http connection for receiving push notifications from a server in the form of [server-sent events](http://dev.w3.org/html5/eventsource/). Mozilla Developer Network has a [good page](https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events) on server-sent events and event source usage too.

### usage

``` objc
TRVSEventSource *eventSource = [[TRVSEventSource alloc] initWithURL:[NSURL URLWithString:@"http://127.0.0.1:8000"]];

[eventSource addListenerForEvent:@"message" usingEventHandler:^(TRVSServerSentEvent *event, NSError *error) {
    NSDictionary *JSON = [NSJSONSerialization JSONObjectWithData:event.data options:0 error:NULL];
    Message *message = [Message messageWithJSON:JSON];
    NSArray *messages = [self.messages arrayByAddingObject:message];
    NSIndexPath *indexPath = [NSIndexPath indexPathForItem:messages.count inSection:0];

    dispatch_async(dispatch_get_main_queue(), ^{
        self.messages = messages;
        [self.collectionView insertItemsAtIndexPaths:@[indexPath]];
    });
}];
```

I wrote a [test server](https://github.com/travisjeffery/TRVSEventSource/blob/master/TRVSEventSourceExample/server.js) that you can run during development too.

`node ./TRVSEventSourceExample/server.js`

```
❯ curl 127.0.0.1:8000
event: message
data: {"id": 1, "body":"1381466575460", "author_id": 1, "conversation_id": 1}

event: message
data: {"id": 2, "body":"1381466577463", "author_id": 1, "conversation_id": 1}
```
