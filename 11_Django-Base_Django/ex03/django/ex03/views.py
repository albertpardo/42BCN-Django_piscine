from django.shortcuts import render

def _rgb_str_list(red_lst, blue_lst, green_lst):
    '''
    Return a list of strings in rgb format for use in HTML
    '''
    result = [f"rgb({r},{g},{b})" for r,g,b in zip(red_lst, blue_lst, green_lst)]
    return result

def _color_table():

    rows = 50;
    maxim = 250;

    maxim_lst = [str(maxim) for x in range(rows)] 
    cero_to_max = [str(x) for x in range(0,maxim,int(maxim/rows))]

    black_shade = _rgb_str_list(cero_to_max, cero_to_max, cero_to_max)
    red_shade = _rgb_str_list(maxim_lst, cero_to_max, cero_to_max)
    blue_shade = _rgb_str_list(cero_to_max, maxim_lst, cero_to_max)
    green_shade = _rgb_str_list(cero_to_max, cero_to_max, maxim_lst)
    
    colors_table = []
    for i in range(rows):
        colors_table.append([ black_shade[i], red_shade[i], blue_shade[i], green_shade[i]])
    return colors_table

def table_view(request):
    colors_table = _color_table()
    return render(request, 'ex03/index.html', {'colors_table' : colors_table})
