import pytest
from src.parser import parser
from src.transformer import ConfigTransformer
from lark import Lark

def parse_and_transform(text):
    tree = parser.parse(text)
    transformer = ConfigTransformer()
    transformer.transform(tree)
    return transformer.vars

def test_numbers_and_strings():
    cfg = '''
    var a := 10;
    var b := 3.14;
    var c := "hello";
    '''
    vars = parse_and_transform(cfg)
    assert vars['a'] == 10
    assert vars['b'] == 3.14
    assert vars['c'] == "hello"

def test_array_and_dict():
    cfg = '''
    var arr := #(1 2 3);
    var d := { x = 10, y = 20 };
    '''
    vars = parse_and_transform(cfg)
    assert vars['arr'] == [1,2,3]
    assert vars['d']['x'] == 10
    assert vars['d']['y'] == 20

def test_const_expressions():
    cfg = '''
    var a := 5;
    var b := 10;
    var sum := ?(+ a b);
    var prod := ?(* a b);
    var diff := ?(- b a);
    var arr := #(1 2 3 4);
    var len_arr := ?(len arr);
    '''
    vars = parse_and_transform(cfg)
    assert vars['sum'] == 15
    assert vars['prod'] == 50
    assert vars['diff'] == 5
    assert vars['len_arr'] == 4

def test_var_ref_and_nested_dict():
    cfg = '''
    var cfg := { max = 100, inner = { value = 42 } };
    var x := cfg.max;
    var y := cfg.inner.value;
    '''
    vars = parse_and_transform(cfg)
    assert vars['x'] == 100
    assert vars['y'] == 42

def test_nested_array_and_dict():
    cfg = '''
    var data := #(
        { a = 1, b = 2 }
        { a = 3, b = 4 }
    );
    '''
    vars = parse_and_transform(cfg)
    assert vars['data'][0]['a'] == 1
    assert vars['data'][1]['b'] == 4
