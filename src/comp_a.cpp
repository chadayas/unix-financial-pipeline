#include<vector>
#include<string>
#include<iostream>
#include<map>

using namespace std;

class Company_A {
public: 	
	Company_A() {};	
	
	Company_A(int rev, int cgs, int so, int sp): 
	revenue(rev), cogs(cgs), shares_out(so), share_price(sp) {}	
	
	auto read_opex(istream& in);	
	Company_A(istream& in); 

	double gross_margin() const {return revenue - static_cast<double>(cogs)/revenue;}
	int gross_profit() const {return revenue - cogs;}
	int market_cap() const {return share_price * shares_out;}
	int op_income(const map<string, int>& m, const int gp);	
	
	void print_financials(const string &name);
	void print_opex(const map<string, int>& r);
	
private:
	int revenue, cogs, shares_out, share_price;

	
};

auto Company_A::read_opex(istream& in){
	map<string, int> ret;
	string s;
	int x;
	while(in >> s >> x)
		ret[s] = x;
	return ret;
}

int Company_A::op_income(const map<string, int>& m, const int gp){
	int total_op = 0;
	for(const auto& dollar_amt : m)
		total_op += dollar_amt.second;
	int op_inc = gp - total_op;
	return op_inc;
}

void Company_A::print_financials(const string &name){
	vector<string> finan{name, "Share price", 
		"Shares Outstanding", "Revenue", "COGS", "Market Cap"};

	vector<int> dollars{00, share_price, shares_out, revenue, cogs, market_cap()};	
	vector<string::size_type> v_sz;
	string::size_type len = 0;	
	for (const auto& x : finan){
		string row = '|' + string(2, ' ') + x + string(2,' ');
		len += row.size();	
		v_sz.push_back(x.size());	
		cout << row;
	}
	cout << '|' << endl;
	cout << string(len+1, '-');
	cout << endl;	
	for (auto i = 0; i != dollars.size(); ++i){
		string dol_str = to_string(dollars[i]);
		string row = '|' + string(2,' ') + to_string(dollars[i]) + 
			string(v_sz[i]+2 -dol_str.size()  , ' ');
		cout << row;	
	}

	cout << '|' << endl;
}

void Company_A::print_opex(const map<string, int>& r){
	string spacer(2,' ');
	string idx_1 = "Operating Expense" + spacer + '|';
	string idx_2 = 	spacer + "$ (in millions)" + spacer + '|';
	string mix = idx_1 + idx_2;	
	cout << mix << endl;
	for (const auto& [item, opex] : r){
		cout << item << string(idx_1.size()+2 - item.size(), ' ') << opex << endl;
	}
}

int main(){
	Company_A nxp(/*revenue= */ 12614, /*COGS=*/5495, 
			/*shares_out=*/252, /*share_price=*/221);
	auto op_map = nxp.read_opex(cin);
	nxp.print_opex(op_map);
}
