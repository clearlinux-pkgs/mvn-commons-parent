#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-parent
Version  : 5
Release  : 7
URL      : https://github.com/apache/commons-parent/archive/commons-parent-5.tar.gz
Source0  : https://github.com/apache/commons-parent/archive/commons-parent-5.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/14/commons-parent-14.pom
Source2  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/11/commons-parent-11.pom
Source3  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/12/commons-parent-12.pom
Source4  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/17/commons-parent-17.pom
Source5  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/18/commons-parent-18.pom
Source6  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/21/commons-parent-21.pom
Source7  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/22/commons-parent-22.pom
Source8  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/23/commons-parent-23.pom
Source9  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/24/commons-parent-24.pom
Source10  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/25/commons-parent-25.pom
Source11  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/28/commons-parent-28.pom
Source12  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/32/commons-parent-32.pom
Source13  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/33/commons-parent-33.pom
Source14  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/34/commons-parent-34.pom
Source15  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/35/commons-parent-35.pom
Source16  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/37/commons-parent-37.pom
Source17  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/38/commons-parent-38.pom
Source18  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/39/commons-parent-39.pom
Source19  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/40/commons-parent-40.pom
Source20  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/41/commons-parent-41.pom
Source21  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom
Source22  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/43/commons-parent-43.pom
Source23  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/45/commons-parent-45.pom
Source24  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/46/commons-parent-46.pom
Source25  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/47/commons-parent-47.pom
Source26  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/5/commons-parent-5.pom
Source27  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/7/commons-parent-7.pom
Source28  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/9/commons-parent-9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-parent-data = %{version}-%{release}
Requires: mvn-commons-parent-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-parent package.
Group: Data

%description data
data components for the mvn-commons-parent package.


%package license
Summary: license components for the mvn-commons-parent package.
Group: Default

%description license
license components for the mvn-commons-parent package.


%prep
%setup -q -n commons-parent-commons-parent-5

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-parent
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-parent/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/14
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/14/commons-parent-14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11/commons-parent-11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/12
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/12/commons-parent-12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17/commons-parent-17.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/18
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/18/commons-parent-18.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/21
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/21/commons-parent-21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22/commons-parent-22.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/23
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/23/commons-parent-23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24/commons-parent-24.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25/commons-parent-25.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/28
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/28/commons-parent-28.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/32
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/32/commons-parent-32.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33/commons-parent-33.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34/commons-parent-34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/35
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/35/commons-parent-35.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37/commons-parent-37.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38/commons-parent-38.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39/commons-parent-39.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/40
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/40/commons-parent-40.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41/commons-parent-41.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42/commons-parent-42.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43/commons-parent-43.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/45
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/45/commons-parent-45.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/46
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/46/commons-parent-46.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47/commons-parent-47.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5/commons-parent-5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7/commons-parent-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9/commons-parent-9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11/commons-parent-11.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/12/commons-parent-12.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/14/commons-parent-14.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17/commons-parent-17.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/18/commons-parent-18.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/21/commons-parent-21.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22/commons-parent-22.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/23/commons-parent-23.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24/commons-parent-24.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25/commons-parent-25.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/28/commons-parent-28.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/32/commons-parent-32.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33/commons-parent-33.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34/commons-parent-34.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/35/commons-parent-35.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37/commons-parent-37.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38/commons-parent-38.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39/commons-parent-39.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/40/commons-parent-40.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41/commons-parent-41.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42/commons-parent-42.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43/commons-parent-43.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/45/commons-parent-45.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/46/commons-parent-46.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47/commons-parent-47.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5/commons-parent-5.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7/commons-parent-7.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9/commons-parent-9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-parent/LICENSE.txt
