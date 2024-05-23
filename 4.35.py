from collections import defaultdict
from typing import List, Tuple

def fill_specializations(specializations: List[Tuple[str, str]]):
    spec_dict = defaultdict(list)
    for spec, name in specializations:
        spec_dict[spec].append(name)
    return dict(spec_dict)
