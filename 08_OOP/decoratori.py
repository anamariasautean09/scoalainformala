# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# print(functie_simpla())


def decorator_depozit(material):
    def wrapper(functia_noastra):
        def wrapper_internal(*args):
            #print(f"Ambalam produse din {functia_noastra.__name__} cu {material}")
            return f"Ambalam produse {functia_noastra.__name__} cu {material}: {', '.join(x for x  in functia_noastra(*args))}"
        return wrapper_internal
    return wrapper


@decorator_depozit("hartie")
def impachetare_carti(*args):
    return args

print(impachetare_carti("Amintiri din copilarie", "Baltagul"))

@decorator_depozit("folie_alimentare")
def impachetare_fructe(*args):
    return args

print(impachetare_fructe("mere", "pere"))