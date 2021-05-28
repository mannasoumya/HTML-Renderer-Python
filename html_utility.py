def html_by_tag(tag_props_dct, subcontent='', closing=True):
    tag_props = tag_props_dct.copy()
    if "type" not in tag_props:
        print(f":ERROR: `type` is a mandatory key")
        raise Exception("MandatoryKeyMissing")

    tag = tag_props.pop("type")
    display = ''
    result = f'<{tag}'
    if "display" in tag_props:
        display = tag_props.pop("display")
    for key in tag_props:
        result = result + f' {str(key)}="{tag_props[key]}"'
    if closing:
        result = result + f'>{display}{subcontent}</{tag}>'
    else:
        result = result + f'>{display}{subcontent}'
    return result


def create_tag(*args):
    dct = {}
    for arg in args:
        assert(len(arg) == 2)
        assert(type(arg) == tuple)
        if arg[0] not in dct:
            dct[arg[0]] = arg[1]
        else:
            print(f":ERROR: Duplicate key `{arg[0]}`.")
            raise Exception("DuplicateKey")

    if "type" not in dct:
        print(f":ERROR: `type` is a mandatory key")
        raise Exception("MandatoryKeyMissing")
    if "type" in dct and dct["type"] == '':
        print(f":ERROR: `type` is a mandatory key whose value needs to be passed")
        raise Exception("MandatoryKeyMissing")
    
    return dct

def join_tags(*args):
    res = ''
    for arg in args:
        res = res+html_by_tag(*arg)
    return res
