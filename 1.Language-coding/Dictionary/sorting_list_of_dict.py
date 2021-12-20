def sort_list_of_dict():
    l = [{"name": "a", "age": 10},
         {"name": "z", "age": 1},
         {"name": "s", "age": 120},
         {"name": "b", "age": 101}
         ]

    sorted_list = sorted(l, key=lambda x: x["age"],reverse=True)
    print(f"sorted_list= {sorted_list}")


if __name__ == "__main__":
    sort_list_of_dict()
