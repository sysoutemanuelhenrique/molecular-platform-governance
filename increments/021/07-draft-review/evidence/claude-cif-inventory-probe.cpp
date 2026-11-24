// Scratch probe (not project code): list mmCIF categories/tags and struct_conn symmetry with Gemmi 0.7.5 DOM.
#include <gemmi/cif.hpp>
#include <iostream>
namespace cif = gemmi::cif;
int main(int argc, char** argv) {
  cif::Document d = cif::read_file(argv[1]);
  for (cif::Block& b : d.blocks) {
    std::cout << "BLOCK " << b.name << "\n";
    for (const std::string& cat : b.get_mmcif_category_names()) {
      cif::Table t = b.find_mmcif_category(cat);
      std::cout << "CAT " << cat << " rows=" << t.length();
      for (const std::string& tag : t.tags()) std::cout << " " << tag.substr(cat.size());
      std::cout << "\n";
    }
    cif::Table sc = b.find("_struct_conn.", {"id", "conn_type_id", "?ptnr1_symmetry", "?ptnr2_symmetry"});
    for (auto r : sc) std::cout << "CONN " << r[0] << " " << r[1] << " " << (r.has(2) ? r[2] : "<absent>") << " " << (r.has(3) ? r[3] : "<absent>") << "\n";
  }
}
