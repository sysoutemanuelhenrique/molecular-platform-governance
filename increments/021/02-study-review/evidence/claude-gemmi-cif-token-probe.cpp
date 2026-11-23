// Scratch probe (not project code): Gemmi 0.7.5 CIF DOM token round-trip.
#include <gemmi/cif.hpp>
#include <gemmi/to_cif.hpp>
#include <iostream>
#include <sstream>
namespace cif = gemmi::cif;
int main() {
  const char* src =
    "data_t\n"
    "loop_\n_x.id\n_x.v\n"
    "1 ?\n2 .\n3 '?'\n4 '.'\n5 'two words'\n6 0.000\n7 1.20(3)\n8 \"it's\"\n9\n;multi\nline\n;\n";
  cif::Document d = cif::read_memory(src, std::strlen(src), "probe");
  cif::Block& b = d.sole_block();
  cif::Table t = b.find("_x.", {"id", "v"});
  for (auto row : t) {
    const std::string& raw = row[1];
    std::cout << row[0] << " raw=[" << raw << "] is_null=" << cif::is_null(raw)
              << " as_string=[" << cif::as_string(raw) << "] quote(raw)=[" << cif::quote(raw) << "]\n";
  }
  // Build a new block, copy raw tokens with add_row, serialize, re-read.
  cif::Document out; out.blocks.emplace_back("derived");
  cif::Loop& loop = out.blocks[0].init_loop("_x.", {"id", "v"});
  for (auto row : t) loop.add_row(std::vector<std::string>{row[0], row[1]});
  std::ostringstream os; cif::write_cif_to_stream(os, out, cif::WriteOptions());
  std::string s = os.str();
  std::cout << "---serialized---\n" << s << "---reread---\n";
  cif::Document d2 = cif::read_memory(s.c_str(), s.size(), "probe2");
  cif::Table t2 = d2.sole_block().find("_x.", {"id", "v"});
  size_t i = 0; bool all_equal = true;
  for (auto row : t2) { auto orig = t[i++]; if (row[1] != orig[1]) { all_equal = false; std::cout << "DIFF id=" << row[0] << "\n"; } }
  std::cout << "raw_tokens_identical_after_roundtrip=" << all_equal << "\n";
}
