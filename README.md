# HTML-Renderer-Python
## Render HTML Pages natively using a Simple Python Top-Level API

### Creating Custom Tags:

All Custom Tags are Python Dictionaries.

Attribute Kinds (API specific):
- `type` : Tag Name
- `display` : Text Node inside display

*Note: `type` is a mandatory attribute for creating a tag.*

**Examples:**

```python
div_tag = {
  "type" : "div"
}

a_tag = {
  "type" : "a",
  "diplay" : "Google",
  "href" : "https://www.google.com/"
}

style_tag = {
  "type" : "style",
  "display" : """
    .table
    {
        padding: 20px;
    }
    .tile
    {
        padding: 20px;
    }
    body
    {
        background: linear-gradient(to right, #fdfaf6 0%, #edffec 100%);
        /*background-repeat: no-repeat;*/
        background-size: auto;
    }
    """
}
```
