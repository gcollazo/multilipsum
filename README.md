# MultiLipsum
This app generates dummy text for using as placeholder content.

---

### Command Line Usage

Default, generates 1 paragraph

    $ ./mlipsum

Generate 3 words

    $ ./mlipsum -f words -n 3

Generate 3 sentences

    $ ./mlipsum -f sentences -n 3

Generate 3 paragraphs

    $ ./mlipsum -f paragraphs -n 3

Generate 3 paragraphs of **auto** content using the -t, --topic argument

    $ ./mlipsum -f pargraphs -n 3 -t auto

---

### Module Usage

Generate normal lipsum text

    from MultiLipsum.core import MultiLipsum
    
    ml = MultiLipsum()
    
    # Print 3 words
    print ml.get_words(3)
    
    # Print 3 sentences
    print ml.get_sentences(3)
    
    # Print 3 paragraphs
    print ml.get_paragraphs(3)

Generate topic specific text

    from MultiLipsum.core import MultiLipsum
    
    ml = MultiLipsum('auto')
    
    # Print 3 words
    print ml.get_words(3)
    
    # Print 3 sentences
    print ml.get_sentences(3)
    
    # Print 3 paragraphs
    print ml.get_paragraphs(3)