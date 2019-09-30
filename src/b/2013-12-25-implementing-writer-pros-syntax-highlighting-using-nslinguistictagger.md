---
layout: post.html
title: "Text processing with NSLinguisticTagger: implementing Writer Pro's syntax control"
date: 2013-12-25 02:02
comments: true
collection: ios
redirectFrom: /b/2013/12/implementing-writer-pros-syntax-highlighting-using-nslinguistictagger/
---

Update: I wrote this code to show that iA was patenting a feature based on a feature baked into iOS' frameworks. Any iOS developer could build the same feature with ten lines of code. John Gruber [linked my project](https://daringfireball.net/linked/2013/12/26/patent-before-christmas) on Daring Fireball. iA dropped their pending patents.

Here's how to implement Writer Pro's syntax highlighting feature with attributed strings and NSLinguisticTagger.

[Project](https://github.com/travisjeffery/LingusticTaggerDemo) on GitHub.

![demo gif](https://raw.github.com/travisjeffery/LingusticTaggerDemo/master/linguistictagger.gif)

``` objc
- (void)highlightLinguisticTag:(NSString *)tag {
    self.textView.attributedText = [self attributedStringHighlightedForTag:tag];
}

- (NSAttributedString *)attributedStringHighlightedForTag:(NSString *)tag {
    NSString *string = @"Some string..."
    NSRange stringRange = NSMakeRange(0, string.length);

    NSMutableAttributedString *text = [[NSMutableAttributedString alloc] initWithString:string attributes:nil];
    [text addAttribute:NSForegroundColorAttributeName value:[UIColor lightGrayColor] range:stringRange];

    NSLinguisticTagger *tagger = [[NSLinguisticTagger alloc] initWithTagSchemes:@[NSLinguisticTagSchemeLexicalClass] options:0];
    tagger.string = string;
    [tagger enumerateTagsInRange:stringRange scheme:NSLinguisticTagSchemeLexicalClass options:0 usingBlock:^(NSString *tokenTag, NSRange tokenRange, NSRange sentenceRange, BOOL *stop) {
        if ([tokenTag isEqualToString:tag]) {
            [text addAttribute:NSForegroundColorAttributeName value:[UIColor blackColor] range:tokenRange];
        }
    }];

    return text;
}
```

Doesn't take much, does it?
