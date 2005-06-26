%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Continuation-based web application framework
Summary(pl):	Szkielet aplikacji WWW oparty na kontynuacji
Name:		ruby-kansas
Version:	0.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1197/kansas_%{version}.tar.gz
# Source0-md5:	247ed7f6cdd9e060cf07d55ebb57f81e
URL:		http://enigo.com/projects/kansas
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kansas is a software package that maps relational database tables to
objects within the Ruby programming language. Kansas was originally
written by Avi Bryant as what he calls a quick hack to play with
object/relational mapping ideas. It was packaged as an extra within
his old Iowa distribution.

%description -l pl
Kansas to pakiet oprogramowania odwzorowuj�cy tabele relacyjnych baz
danych na obiekty w j�zyku programowania Ruby. Kansas zosta�
pierwotnie napisany przez Avi Bryanta jako (wg. autora) szybki hack do
zabawy z pomys�ami odwzorowa� obiektowo-relacyjnych. By� pakietowany
jako dodatek w jego starej dystrybucji Iowa.

%prep
%setup -q -n kansas_%{version}

%build
cp %{_datadir}/setup.rb .
mkdir lib
mv kansas* lib/

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
rm $RPM_BUILD_ROOT%{ruby_ridir}/Array/cdesc-Array.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/Object/cdesc-Object.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/String/cdesc-String.yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/kansas.rb
%{ruby_rubylibdir}/kansas
%{ruby_ridir}/KS*
%{ruby_ridir}/Kansas*
